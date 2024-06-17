from flask import Flask, render_template, request, redirect, url_for, session
import os
import ujson
import json

script_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # replace with your own secret key

def read_json(file_path: str):
    "Read a JSON file."
    with open(file_path, "r") as f:
        data = ujson.load(f)
    return data

# Load the JSON data
reranked_trials_reloaded = read_json(os.path.join(script_dir, "p6_evaluated_trials_0.json"))

# Custom filter to replace newlines with <br> tags
@app.template_filter('nl2br')
def nl2br(value):
    return value.replace('\n', '<br>')

@app.route('/', methods=['GET', 'POST'])
def survey():
    if 'current_trial_index' not in session:
        session['current_trial_index'] = 0

    current_trial_index = session['current_trial_index']

    # Ensure the current_trial_index is within the range
    if current_trial_index >= len(reranked_trials_reloaded):
        session['current_trial_index'] = 0
        current_trial_index = 0

    trial = reranked_trials_reloaded[current_trial_index]

    if request.method == 'POST':
        results = request.form.to_dict()
        author = results.get('author', None)

        # Add a validation check for the author
        if not author:
            error_message = "Please select an author before submitting."
            return render_template('survey.html', trial=trial, error_message=error_message, previous_results=results)

        # Check if all criteria are filled
        missing_items = []
        for section, nested_criteria in trial['structured_criteria'].items():
            for term, criteria_list in nested_criteria.items():
                real_criteria = criteria_list[1]
                for item in real_criteria:
                    if isinstance(item, str):
                        key = f"{term}|{item}"
                        if key not in results:
                            missing_items.append(item)
                    elif isinstance(item, list):
                        for subitem in item:
                            key = f"{term}|{subitem}"
                            if key not in results:
                                missing_items.append(subitem)
                        unique_id = f"{term}_global{real_criteria.index(item) + 1}"
                        if unique_id not in results:
                            missing_items.append("is the overall criterion met?")

        if missing_items:
            error_message = "Please answer all questions before submitting. Missing items: " + ", ".join(missing_items)
            return render_template('survey.html', trial=trial, error_message=error_message, previous_results=results)

        # Load existing results
        results_filename = 'results.json'
        if os.path.exists(results_filename):
            with open(results_filename, 'r') as f:
                all_results = json.load(f)
        else:
            all_results = {}

        # Check if the author already submitted results for this nctId
        nctId = trial['nctId']
        if nctId in all_results and author in all_results[nctId]:
            error_message = f"Author {author} has already submitted results for trial {nctId}."
            return render_template('survey.html', trial=trial, error_message=error_message, previous_results=results)

        # Save the new results, preserving the original nested structure
        if nctId not in all_results:
            all_results[nctId] = {}

        structured_results = {}
        for section, nested_criteria in trial['structured_criteria'].items():
            structured_results[section] = {}
            for term, criteria_list in nested_criteria.items():
                real_criteria = criteria_list[1]
                structured_results[section][term] = [criteria_list[0], []]
                for item in real_criteria:
                    if isinstance(item, str):
                        key = f"{term}|{item}"
                        structured_results[section][term][1].append(results[key])
                    elif isinstance(item, list):
                        sublist = []
                        for subitem in item:
                            key = f"{term}|{subitem}"
                            sublist.append(results[key])
                        structured_results[section][term][1].append(sublist)
                        unique_id = f"{term}_global{real_criteria.index(item) + 1}"
                        if unique_id in results:
                            structured_results[section][term][1].append(results[unique_id])

        all_results[nctId][author] = structured_results

        with open(results_filename, 'w') as f:
            json.dump(all_results, f, indent=4)

        session['current_trial_index'] += 1

        if session['current_trial_index'] >= len(reranked_trials_reloaded):
            return render_template('change_author.html')

        return redirect(url_for('survey'))

    return render_template('survey.html', trial=trial, error_message=None, previous_results={})

@app.route('/change_author', methods=['POST'])
def change_author():
    # Remove the current author from the session
    session.pop('current_trial_index', None)
    # Redirect back to the main page
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5002)

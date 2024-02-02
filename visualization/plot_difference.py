import matplotlib.pyplot as plt
import pandas as pd

# Data for visualization
data = {
    'accuracy_adjusted': {1: 0.9425431207367014, 2: 0.9678519785642111, 3: 0.570402538081684, 4: 0.47021671216036276, 5: 0.4452564299291284, 6: 0.8134970150172958, 7: 0.34664665221657276, 8: 0.09280201379437389, 9: 0.5283677668854758, 10: 0.545550451187241},
    'relevance_adjusted': {1: 0.7728499565342642, 2: 0.08823115094882501, 3: 0.00047497163927181536, 4: 0.32863566852894716, 5: 0.0342002511584492, 6: 0.16609638322291123, 7: 0.8701938642108918, 8: 0.2899586744853867, 9: 0.04834884732546354, 10: 0.057556575722834694},
    'creativity_adjusted': {1: 0.021756538101806666, 2: 0.11709028757487581, 3: 0.10628800217445389, 4: 0.31850303990336615, 5: 0.4406388434994682, 6: 0.479127599930392, 7: 0.2048067215049699, 8: 0.15920834266848308, 9: 0.04447418708506674, 10: 0.6796150479037307},
    'specificity_adjusted': {1: 0.7427236085473201, 2: 0.12149596530944919, 3: 0.0068382254359392524, 4: 0.051253014435360164, 5: 0.41989335868152183, 6: 0.0008846903460989959, 7: 0.7165583658200755, 8: 0.019581762649902298, 9: 0.027505285194681636, 10: 0.5538761345574577},
    'feasibility_adjusted': {1: 0.36839712584441425, 2: 0.5760589639289975, 3: 0.534388732753105, 4: 0.9656175639483721, 5: 0.4620262353364921, 6: 0.11118330618043991, 7: 0.9265926193540353, 8: 0.9173529703929373, 9: 0.7923239827092728, 10: 0.8248857723246986}
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(15, 8))

# Multiple bar plots
df.plot(kind='bar', ax=plt.gca())
plt.title('ANOVA Results for Different Metrics')
plt.xlabel('Task Index')
plt.ylabel('Scores')
plt.xticks(range(0, 10), range(1, 11))  # Adjusting x-ticks for text index
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Metrics')

# Show the plot
plt.show()



###################
import matplotlib.pyplot as plt
import pandas as pd

# Data for visualization
data = {'accuracy_adjusted': {1: 0.9313798863727404,
   2: 0.9781515676704196,
   3: 0.19355258958106478,
   4: 0.44902761602000074,
   5: 0.49541035796582367,
   6: 0.5590775233822863,
   7: 0.7924885179693003,
   8: 0.08131101409517259,
   9: 0.038266267110489055,
   10: 0.5438786676042202},
  'relevance_adjusted': {1: 0.43618738327363726,
   2: 0.15627791840028563,
   3: 0.0021459048253824574,
   4: 0.24298775601482842,
   5: 0.029822646278451045,
   6: 0.1278098641984019,
   7: 0.8644667445641319,
   8: 0.2280828752072778,
   9: 0.07268581930391793,
   10: 0.047462095765889195},
  'creativity_adjusted': {1: 0.02515026685730645,
   2: 0.12560603507565943,
   3: 0.14091385116097757,
   4: 0.4088666563143329,
   5: 0.28826560441078036,
   6: 0.5509627378564559,
   7: 0.16400194901144963,
   8: 0.05126619431608793,
   9: 0.10161390940247278,
   10: 0.744936199489955},
  'specificity_adjusted': {1: 0.5718607332246237,
   2: 0.22330751614999023,
   3: 0.007189034300098941,
   4: 0.06831871318426112,
   5: 0.4051917787430913,
   6: 0.003260278702300568,
   7: 0.49277780939978866,
   8: 0.020910370638489453,
   9: 0.024423642876812392,
   10: 0.639301349826352},
  'feasibility_adjusted': {1: 0.2451075691755776,
   2: 0.6463349503556584,
   3: 0.794979257396712,
   4: 0.9899937777177213,
   5: 0.36204972877185787,
   6: 0.06564990143361045,
   7: 0.9564993360800019,
   8: 0.8062347667254676,
   9: 0.7218633498397802,
   10: 0.44727170536520156}}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(15, 8))

# Multiple bar plots
df.plot(kind='bar', ax=plt.gca())
plt.title('Kruskall-Wallis Test Results for Different Metrics')
plt.xlabel('Task Index')
plt.ylabel('Scores')
plt.xticks(range(0, 10), range(1, 11))  # Adjusting x-ticks for text index
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Metrics')

# Show the plot
plt.show()
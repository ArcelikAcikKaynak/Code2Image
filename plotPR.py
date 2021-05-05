import os
from FCNdense import FCN_model 
import tensorflow as tf
from generator import Generator 
import numpy as np
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc
from matplotlib import pyplot
from sklearn.metrics import matthews_corrcoef

def precision(a,b):
  return a/(a+b)
def recall(a,b):
  return a/(a+b)
def f1(a,b):
  return 2*a*b/(a+b)

model = FCN_model(len_classes=2, dropout_rate=0.2)

#load the model..change the path accordingly
model.load_weights('./Pretrained_Models/CWE119/model_epoch_037_loss_0.277_acc_0.900_val_loss_0.193_val_acc_0.946.h5')

val_generator = Generator('test', BATCH_SIZE=2)


##This is for CWE-119 
TP119 = 0
FP119 = 0
TN119 = 0
FN119 = 0

proball = []
true_class_all = []


for i in range(len(val_generator)):
  if i%500 == 0:
    print(i, "out of ", len(val_generator))

  prediction_probs = np.array(model.predict(val_generator[i][0])) # predict probabilities

  prediction_probs = prediction_probs[:,1]

  true_class = np.array(val_generator[i][1])[:,0]

  for k in range(len(true_class)):

    true_class_all.append(int(true_class[k]))

  proball = np.append(proball, prediction_probs)



lr_precision, lr_recall, thresholds = precision_recall_curve(true_class_all, proball)
print("pr ", lr_precision)
print("re ",lr_recall)
print("thr ", thresholds)

best_mcc = 0.0
for thr in  thresholds:
  y_pred = (proball >= thr).astype(int)
  score = matthews_corrcoef(true_class_all, y_pred)
  if (score > best_mcc):
    best_mcc = score
print("mcc: ", best_mcc)


lr_auc =  auc(lr_recall, lr_precision)

print('CWE 119: auc=%.3f' % (lr_auc))


with open('saveprecision119.npy', 'wb') as f:
    np.save(f,lr_precision)

with open('saverecall119.npy', 'wb') as f:
    np.save(f,lr_recall) 


f1_scores = 2*np.multiply(lr_precision,lr_recall)/np.add(lr_precision,lr_recall)

f1_scores[np.isnan(f1_scores)] = 0

print("f1", f1_scores )

f1max = np.max(f1_scores)
print("max f1 ", f1max)

f1maxindex = np.where(f1_scores == f1max)

print("precision f1max=", lr_precision[f1maxindex] )
print("recall f1max=", lr_recall[f1maxindex] )


pyplot.plot(lr_recall, lr_precision, marker='.', label='CWE-119')
# axis labels
pyplot.xlabel('Recall')
pyplot.ylabel('Precision')
# show the legend
pyplot.legend()
pyplot.savefig('PR119.png')

 
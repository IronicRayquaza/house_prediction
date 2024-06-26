import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from sklearn import ensemble
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import  train_test_split
import pickle
import sklearn.metrics as sk
import math

#loading data
global data
global clf

data=pd.read_csv("kc_house_data.csv")

print("\n\nWELCOME TO HOUSE PREDICTION MODEL\n\n")

def main():
  while True:
    print("\nPress 1 for USER") 
    print("Press 2 for ADMIN")
    print("Press 3 to exit")
    ch=int(input("\nEnter Choice to continue : ")) 
    if ch==1:
      user() 
    elif ch==2:
      pas=input("\nEnter Password to continue : ") #currently password is PASSWORD
      if(pas=='PASSWORD'):
        admin()
      else:
        print("\nIncorrect Password!!\nAccess Denied")
        main()
    elif ch==3:
      print("\nTHANK YOU FOR USING OUR PROGRAM")
      quit()
      break
    else:
      print("\nWrong Choice Entered!!\nEnter Correct Choice....")
      main()

def user():
  reg=LinearRegression()

  labels=data['price']
  conv_dates=[1 if values==2014 else 0 for values in data.date]
  data['date']=conv_dates
  train1=data.drop(['id','price','date'],axis=1)

  or_count = labels.shape[0]

  x_train,x_test,y_train,y_test = train_test_split(train1,labels,test_size=0.20,random_state=2)

  expected = y_test

  clf=ensemble.GradientBoostingRegressor(n_estimators=500,max_depth=6,min_samples_split=2,learning_rate=0.1,loss='huber')
  clf.fit(x_train,y_train)

  print("\nPROGRAM READY FOR MAKING PREDICTIONS\n\n")
  bed=int(input("Enter number of bedrooms : "))
  bath=float(input("Enter number of bathrooms : "))
  sqft_liv=int(input("Enter Living Area in sqft : "))
  sqft_lot=int(input("Enter Total Area in sqft : "))
  fl=float(input("Enter number of floors : "))
  wf=int(input("Enter 0 if waterfront not available, else enter 1 : "))
  v=int(input("Enter Number of views : "))
  con=int(input("Enter Condition marks : "))
  grd=int(input("Enter Grade : "))
  sqft_abv=int(input("Enter Living Space above the Ground : "))
  sqft_base=int(input("Enter Basement Area : "))
  built=int(input("Enter Year Built : "))
  renovtd=int(input("Enter Year when house Renovated, else 0 : "))
  zc=int(input("Enter ZipCode : "))
  lat=float(input("Enter latitude : "))
  lon=float(input("Enter longitude : "))
  sqft_liv15=int(input("Enter average living area of closest 15 houses : "))
  sqft_lot15=int(input("Enter average total area of closest 15 houses : "))
  new_data=[[bed,bath,sqft_liv,sqft_lot,fl,wf,v,con,grd,sqft_abv,sqft_base,built,renovtd,zc,lat,lon,sqft_liv15,sqft_lot15]]
  print(clf.predict(new_data))
  print("\nTHANK YOU FOR USING OUR HOUSE PRICE PREDICTOR\nWe hope you'll come back to us!!\n")

def admin():
  while True:
    print("Enter 1 to view data")
    print("Enter 2 to visualize data")
    print("Enter 3 to see predicitons data")
    print("Enter 4 to go back to main menu")
    print("Enter 5 to exit")
    ch_admin=int(input("\nEnter Correct Choice  to continue: "))
    if ch_admin==1:
      view_data()
    elif ch_admin==2:
      visl()
    elif ch_admin==3:
      prd()
    elif ch_admin==4:
      main()
      break
    elif ch_admin==5:
      quit()
      break
    else:
      print("\nWrong Choice Entered!\nEnter Correct Choice..")
    

def view_data():
  while True:
    print("\nEnter 1 to check data size")
    print("Enter 2 to view rows")
    print("Enter 3 to go to back")
    ch_view_data=int(input("\nEnter Correct Choice : "))
    if ch_view_data==1:
      print(data.shape)
    elif ch_view_data==2:
      n=int(input("\nEnter number of rows to view : \n"))
      print(data.head(n))
    elif ch_view_data==3:
      admin()
      break
    else:
      print("\nWrong Choice Entered!!Please enter correct choice...")

def visl():
  while True:
    print("\nEnter 1 to Print Mathematical Data")
    print("Enter 2 to Plot graphs")
    print("Enter 3 to go back")
    ch_visl=int(input("\nEnter Correct Choice : "))
    if ch_visl==1:
      print(data.describe())
    elif ch_visl==2:
      graphs()
    elif ch_visl==3:
      admin()
      break
    else:
      print("\nWrong Choice Entered!!Please enter correct choice")


def graphs():
  while True:
    print("\nWELCOME TO GRAPH PLOTTING MODULE\n")
    print("Press 1 for heatmap plot")
    print("Press 2 for plot of Number of Houses according to Number of bedrooms and bathrooms")
    print("Press 3 for plot of Location")
    print("Press 4 for plot of Price Relations")
    print("Press 5 to go back to visualisation")
    ch_graphs=int(input("\nEnter Correct Choice : "))
  
    if ch_graphs==1:
      plt.figure(figsize=(12,10))
      sns.heatmap(data.corr(),cmap="Reds")
      plt.show()
    elif ch_graphs==2:
      fig, axs = plt.subplots(1, 1, tight_layout = True)
      axs.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.5,alpha = 0.6) 
      n_bins = 20
      x=data.bedrooms
      y=data['bedrooms'].value_counts
      N, bins, patches = axs.hist(x,bins = n_bins)
      fracs = ((N**(1 / 5)) / N.max())
      norm = colors.Normalize(fracs.min(), fracs.max())
      for thisfrac, thispatch in zip(fracs, patches):
          color = plt.cm.viridis(norm(thisfrac))
          thispatch.set_facecolor(color)
      plt.xlabel("No. of bedrooms")
      plt.ylabel("No. of House")
      plt.title('No. of houses vs bedrooms')
      plt.show()
      print()
      print()
      fig, axs = plt.subplots(1, 1, tight_layout = True)
      axs.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.5,alpha = 0.6) 
      n_bins = 20
      x=data.bathrooms
      y=data['bathrooms'].value_counts
      N, bins, patches = axs.hist(x,bins = n_bins)
      fracs = ((N**(1 / 5)) / N.max())
      norm = colors.Normalize(fracs.min(), fracs.max())
      for thisfrac, thispatch in zip(fracs, patches):
          color = plt.cm.viridis(norm(thisfrac))
          thispatch.set_facecolor(color)
      plt.xlabel("No. of bathrooms")
      plt.ylabel("No. of House")
      plt.title('No. of houses vs bathrooms')
      plt.show()
    if ch_graphs==3:
      plt.figure(figsize=(10,10))
      sns.jointplot(x=data.lat.values, y=data.long.values, size=10)
      plt.ylabel("Longitude")
      plt.xlabel("Latitude")
      plt.show()
      print()
    if ch_graphs==4:
      #price vs bedrooms
      plt.figure(figsize=(10,10))
      ax = sns.boxplot(data=data, x='bedrooms', y='price', palette='Set2', linewidth=2.5)
      ax.set(title='price vs bedrooms', xlabel='No. of bedrooms', ylabel='Price')
      plt.show()
      #price vs bathrooms
      plt.figure(figsize=(10,10))
      ax = sns.boxplot(data=data, x='bathrooms', y='price', palette='Set2', linewidth=2.5)
      ax.set(title='price vs bathrooms', xlabel='No. of bathrooms', ylabel='Price')
      plt.show()    
      #price vs area
      plt.scatter((data['sqft_living']+data['sqft_basement']),data['price'])
      plt.xlabel("Total Area")
      plt.ylabel("Price")
      plt.title("Price vs Area")
      plt.show() 
      print()   
      #price vs location 3
      plt.scatter(data.waterfront,data.price)
      plt.xlabel("Waterfront")
      plt.ylabel("Price")
      plt.title("Price vs Waterfront")
      plt.show() 
      print()  
      #price vs No. of floors
      plt.scatter(data.floors,data.price)
      plt.xlabel("No. of floors")
      plt.ylabel("Price")
      plt.title("Price vs No. of floors")
      plt.show()
      print()   
      #price vs condition
      plt.scatter(data.condition,data.price)
      plt.xlabel("Coniditon")
      plt.ylabel("Price")
      plt.title("Price vs Condition")
      plt.show()
      print()
      #price vs grade
      plt.scatter(data.grade,data.price)
      plt.xlabel("Grade")
      plt.ylabel("Price")
      plt.title("Price vs Grade")
      plt.show()
      print()
      #price vs Year Built
      plt.scatter(data.yr_built,data.price)
      plt.xlabel("Year Built")
      plt.ylabel("Price")
      plt.title("Price vs Year Built")
      plt.show()
      print()
    elif ch_graphs==5:
      visl()
      break
    else:
      print("\nWrong Choice Entered!!Please Enter correct choice...")

def prd():
  print("\nWELCOME TO PREDICTION MODULE")
  print("\nPROGRAM READY TO MAKE PREDICTION....\n")

  reg=LinearRegression()

  labels=data['price']
  conv_dates=[1 if values==2014 else 0 for values in data.date]
  data['date']=conv_dates
  train1=data.drop(['id','price'],axis=1)

  or_count = labels.shape[0]

  x_train,x_test,y_train,y_test = train_test_split(train1,labels,test_size=0.20,random_state=2)

  expected = y_test

  clf=ensemble.GradientBoostingRegressor(n_estimators=600,max_depth=7,min_samples_split=2,learning_rate=0.1,loss='huber')
  clf.fit(x_train,y_train)
  print("\nTesting Accuracy : ",clf.score(x_test,y_test)*100)
  print("\nTraining Accuracy : ",clf.score(x_train,y_train)*100)
  print("\n")
  p_values = clf.predict(x_test)

  print("Explained Variance Score = ",sk.explained_variance_score(expected,p_values))

  print("Mean Absolute Percentage Error = ",sk.mean_absolute_percentage_error(expected,p_values))

  print("r squared value = ",sk.r2_score(expected,p_values))

  original_params = {'n_estimators': 600, 'max_depth': 7,'min_samples_split': 2,'random_state': 2,'learning_rate': 0.1,'loss':'huber'}
  params = dict(original_params)

  reg.fit(x_train,y_train)
  t_sc = np.zeros((params['n_estimators']),dtype=np.float64)
  y_pred = p_values
  for i,y_pred in enumerate(clf.staged_predict(x_test)):
      t_sc[i]=clf.loss_(y_test,y_pred)

  testsc = np.arange((params['n_estimators']))+1

  plt.figure(figsize=(12, 6))
  plt.subplot(1, 2, 1)
  plt.plot(testsc,clf.train_score_,'b-',label= 'Set dev train')
  plt.plot(testsc,t_sc,'r-',label = 'set dev test')

  with open("Prd.pickle",'wb') as f:
    pickle.dump(p_values,f)

  newfile=pd.DataFrame(y_test)
  newfile['Prediction']=p_values
  newfile.to_csv('prediction_final.csv')

  plt.figure(figsize=(10,10))
  plt.scatter(expected, p_values, c='crimson')
  plt.yscale('log')
  plt.xscale('log')

  p1 = max(max(p_values), max(expected))
  p2 = min(min(p_values), min(expected))
  plt.plot([p1, p2], [p1, p2], 'b-')
  plt.xlabel('Expected Values : ', fontsize=15)
  plt.ylabel('Predicted Values : ', fontsize=15)
  plt.axis('equal')
  plt.show()

main()

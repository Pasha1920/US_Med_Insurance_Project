#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[157]:


#importing required libraries
import csv
import math


# In[158]:


#creating empty lists to store each attribute
ages=[]
sexes=[]
bmis=[]
children=[]
smoker=[]
regions=[]
charges=[]


# In[159]:


def load_list_data(lst,file,column_name):
    with open(file) as csv_file:
        csv_dict=csv.DictReader(csv_file)
        
        for row in csv_dict:
            lst.append(row[column_name])
    return lst


# In[160]:


load_list_data(ages,"insurance.csv","age")
load_list_data(sexes,"insurance.csv","sex")
load_list_data(bmis,"insurance.csv","bmi")
load_list_data(children,"insurance.csv","children")
load_list_data(smoker,"insurance.csv","smoker")
load_list_data(regions,"insurance.csv","region")
load_list_data(charges,"insurance.csv","charges")


# In[161]:


class PatientsInformation:
    #init method that accepts parameters
    def __init__(self,patients_ages,patients_sexes,patients_bmis,patients_num_children,patients_smoker_statuses,patients_regions,patients_charges):
        self.patients_ages=patients_ages
        self.patients_sexes=patients_sexes
        self.patients_bmis=patients_bmis
        self.patients_num_children=patients_num_children
        self.patients_smoker_statuses=patients_smoker_statuses
        self.patients_regions=patients_regions
        self.patients_charges=patients_charges
    
    #calculating average age in insurance database
    def analyze_ages(self):
        total_age=0
        for age in self.patients_ages:
            total_age+=int(age)
        
        return("Average Patient Age="+str(round(total_age/len(self.patients_ages),2))+"years")
    
    #calculating gender distribution % in database
    def analyze_sexes(self):
        male_count=0
        female_count=0
        for sex in self.patients_sexes:
            if sex=="female":
                female_count+=1

            elif sex=="male":
                male_count+=1
        percent_f=round((female_count/len(self.patients_sexes))*100,2)
        percent_m=round((male_count/len(self.patients_sexes))*100,2)
        
        print("Percent females in database:"+str(percent_f)+"%")
        print("Percent males in database:"+str(percent_m)+"%")
    
    #method to find average bmi by gender
    def avg_bmi(self):
        bmi_male_total=0
        bmi_female_total=0
        
        for i in range(0,len(self.patients_bmis)):
            if self.patients_sexes[i]=="male":
                bmi_male_total+=float(self.patients_bmis[i])
            
            else:
                bmi_female_total+=float(self.patients_bmis[i])
        
        avg_male_bmi=round(bmi_male_total/len(self.patients_bmis),2)
        avg_female_bmi=round(bmi_female_total/len(self.patients_bmis),2)
        
        print("Average male bmi="+str(avg_male_bmi))
        print("Average female bmi="+str(avg_female_bmi))
    
    #method to find the unique regions that patients are from
    def unique_regions(self):
        unique_regions=[]
        for region in self.patients_regions:
            if region not in unique_regions:
                unique_regions.append(region)
        
        return unique_regions
    
    #method to find average children per patient
    def avg_children(self):
        total_children=0
        for child_count in self.patients_num_children:
            total_children+=float(child_count)
        
        avg_children=math.floor(total_children/len(self.patients_num_children))
        
        return avg_children
    
    #method to find smoker distribution by gender in dataset
    def smoker_distribution(self):
        male_smokers=0
        female_smokers=0
        for i in range(0,len(self.patients_smoker_statuses)):
            if (self.patients_sexes[i]=="male" and self.patients_smoker_statuses[i]=="yes"):
                male_smokers+=1
            
            elif (self.patients_sexes[i]=="female" and self.patients_smoker_statuses[i]=="yes"):
                female_smokers+=1
        
        percent_smoker_f=round((female_smokers/len(self.patients_smoker_statuses))*100,2)
        percent_smoker_m=round((male_smokers/len(self.patients_smoker_statuses))*100,2)
        
        
        print("Percent of female smokers="+str(percent_smoker_f)+"%")
        print("Percent of male smokers="+str(percent_smoker_m)+"%")
    
    #method to find average insurance charges
    def average_insurance_charges(self):
        total_charges=0
        for charge in self.patients_charges:
            total_charges+=float(charge)

        avg_charge=round(total_charges/len(self.patients_charges),2)
              
        return("Average insurance charges=$"+str(avg_charge))


# In[ ]:





# In[162]:


#Creating object of class PatientsInformation
patients_info=PatientsInformation(ages,sexes,bmis,children,smoker,regions,charges)


# In[163]:


#Printing outcomes of analysis


# In[164]:


#Average age of patient
patients_info.analyze_ages()


# In[165]:


#Male-Female distribution in dataset
patients_info.analyze_sexes()


# In[166]:


#Average bmi by gender
patients_info.avg_bmi()


# In[167]:


#Unique regions
patients_info.unique_regions()


# In[168]:


#Average children (rounded down to the nearest integer)
patients_info.avg_children()


# In[169]:


#Percentage of smokers by gender
patients_info.smoker_distribution()


# In[170]:


#Average Insurance Charges
patients_info.average_insurance_charges()


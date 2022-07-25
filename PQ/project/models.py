from django.db import models

class projects(models.Model):
	Project = models.CharField(max_length=200, null=True)
	SOW = models.TextField()
	Start_date = models.DateField(max_length=200, null=True)
	End_date = models.DateField(null=True)
	Value = models.CharField(max_length=200, null=True)
	customer = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	Contract_No = models.CharField(max_length=200, null=True)
	Project_Manager = models.CharField(max_length=200, null=True)
	End_User_Contact = models.CharField(max_length=200, null=True)
	STATUS = (('Completed ', 'Completed '),('On-Going', 'On-Going'),('Valuations', 'Valuations'),)
	status = models.CharField(max_length=200, null=True,choices=STATUS)

class bids(models.Model):
	Bid_name = models.CharField(max_length=200, null=True)
	Reference_number = models.CharField(max_length=200, null=True)
	End_user = models.CharField(max_length=200, null=True)
	work_category = models.CharField(max_length=200, null=True)
	Last_date_inquiries = models.DateTimeField(max_length=200, null=True)
	Deadline = models.DateTimeField(max_length=200, null=True)
	Bid_opening_date = models.DateTimeField(max_length=200, null=True)
	Bid_value = models.FloatField(max_length=200, null=True)
	Are_you_Interest = models.BooleanField(max_length=200, null=True)
	Did_you_bought = models.BooleanField(max_length=200, null=True)
	File_downloaded = models.BooleanField(max_length=200, null=True)
	Failed_To_Submit = models.BooleanField(max_length=200, null=True)
	WIN = models.BooleanField(max_length=200, null=True)
	SOW = models.TextField(null=True)
	Execution_plan = models.TextField(null=True)
	Execution_place = models.TextField(null=True)

"""
class bid_BOQ(models.Model):
	Item_no = models.CharField(max_length=200, null=True)
	Item_name = models.CharField(max_length=200, null=True)
	Unit = models.CharField(max_length=200, null=True)
	Item_description = models.TextField(null=True)
	Mandatory_List = models.BooleanField(null=True)
	Code = models.CharField(max_length=200,null=True)
	#bids = models.ForeignKey(bids, null=True,on_delete=models.SET_NULL)

"""

class bid_BOQ(models.Model):
	Item_no = models.CharField(max_length=200, null=True)
	Item_name = models.CharField(max_length=200, null=True)


#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def home():
    #return "Hello, Flask!"
from scipy.spatial import distance
from flask import *
import numpy as np
app = Flask(__name__)  
@app.route('/', methods=['GET', 'POST']) 
def message():  
    if request.method == "POST":
       # getting input with name = fname in HTML form
        company = request.form.get("company")
       # getting input with name = lname in HTML form
    #    trigger = int(request.form.get("trigger"))
        trigger = int(request.form.get("trigger"))
    #     if trigger_str:
    #         trigger = int(trigger_str)
    #     else:
    # # Handle the case when trigger_str is empty
    #         trigger = 0  # or any other default value you want to use
    # size = int(request.form.get("size"))
    # new_data = [trigger, company]
    # print(new_data)
#    dist_scipyL = distance.euclidean([1.110970996216897, 152.40857503152347], new_data)
#    dist_scipyM = distance.euclidean([1.1104651162790693,10000.802325581399], new_data)
#    dist_scipyH = distance.euclidean([1.182692307692307, 5000.000000000003], new_data)
    # point1 = np.array((trigger, company))
    # pointL = np.array((1.110970996216897, 152.40857503152347))
    # pointM = np.array((1.1104651162790693,10000.802325581399))
    # pointH = np.array((1.182692307692307, 1.1104651162790693))
        sum_sqL = 1.110970996216897 - trigger
        sum_sqM = 1.1104651162790693 - trigger
        sum_sqH = 1.182692307692307 - trigger

    # finding sum of squares
        if sum_sqL < sum_sqM and sum_sqL < sum_sqH :
            return "Low Band"
        elif sum_sqM < sum_sqH :
            return "Medium Band"
        else :
            return "High Band"
    return render_template("web.html")
if __name__ == '__main__':  
   app.run(debug = True)

import csv
import datetime
now = datetime.date.today()
def call(name,identity):
    if (name=='Date : '):
        with open(identity+'.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([name,"{}.".format(now)])
    else:
        with open(identity+'.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([name, 'present'])
            
            
        
        '''filewriter.writerow(['Derek', 'Software Developer'])
        filewriter.writerow(['Steve', 'Software Developer'])
        filewriter.writerow(['Paul', 'Manager'])
        filewriter.writerow(['ashwin', 'project Manager'])'''
        
        
        



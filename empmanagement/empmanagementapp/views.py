from django.shortcuts import render, redirect
from django.http import HttpResponse
from empmanagementapp.models import EmpDetails
import xlrd
from django.core.files.storage import FileSystemStorage
import openpyxl
from .fusioncharts import FusionCharts

# Create your views here.
def employee_layout(request):
    return render(request, 'layout.html')

def add_employee(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        empcode = request.POST.get('Code')
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        contact = request.POST.get('ContactNo')
        employee = EmpDetails(code_no=empcode, name=name,email_id=email,contact_no=contact)
        employee.save()
        return redirect('/add')

def show_employee(request):
    emp = {}
    employee = EmpDetails.objects.all()
    for e in employee:
      emp = {'employee': employee}
    return render(request, 'show.html', context=emp)

def edit_employee(request, code_no):
    if request.method == 'GET':
      employee = EmpDetails.objects.get(code_no=code_no)
      show = {
          "code_no":employee.code_no,
          "name": employee.name,
          "email_id": employee.email_id,
          "contact_no": employee.contact_no
        }    

      return render(request, 'edit.html', context=show)

    elif request.method == 'POST':
        name = request.POST.get("Name")
        email_id = request.POST.get("Email")
        contact_no = request.POST.get("ContactNo")
        employee = EmpDetails.objects.get(code_no=code_no)
        employee.name = name
        employee.email_id = email_id
        employee.contact_no = contact_no
        employee.save()
        return redirect("/show")

def delete_employee(request, code_no):
    employee = EmpDetails.objects.get(code_no=code_no)
    employee.delete()
    return redirect('/show')

def upload_file(request):
    if "GET" == request.method:
        return render(request, 'upload.html', {})
    else:
        excel_file = request.FILES['excel_file']
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        print(worksheet)
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
            employee = EmpDetails(
              code_no=row_data[0], name=row_data[1], email_id=row_data[2], contact_no=row_data[3])
            employee.save()
            employee = EmpDetails.objects.all()

        return render(request, 'show.html', context={'employee': employee})  

def search_employee(request):

    if request.method == 'GET':
        return render(request, 'search.html')

    elif request.method == 'POST':
        name = request.POST.get("Name")
        print(name)
        employee = EmpDetails.objects.filter(name__iregex = name)
      
        return render(request, 'search.html', context={"data": employee})

def chart(request):
   chartObj = FusionCharts( 'gantt', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "New Store Opening - Project Plan",
    "dateformat": "dd/mm/yyyy",
    "outputdateformat": "ddds mns yy",
    "ganttwidthpercent": "100",
    "ganttpaneduration": "40",
    "ganttpanedurationunit": "d",
    "useverticalscrolling": "0",
    "plottooltext": "<b>$label</b><br>Start: <b>$start</b><br>End: <b>$end</b>",
    "theme": "fusion"
  },
  "connectors": [
    {
      "connector": [
        {
          "fromtaskid": "1-1",
          "totaskid": "2-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "2-1",
          "totaskid": "3-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "3-1",
          "totaskid": "4-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "4-1",
          "totaskid": "5-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "5-1",
          "totaskid": "6-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "6-1",
          "totaskid": "7-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "7-1",
          "totaskid": "8-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "8-1",
          "totaskid": "9-1",
          "color": "#F2726F",
          "thickness": "2"
        },
        {
          "fromtaskid": "9-1",
          "totaskid": "10-1",
          "color": "#F2726F",
          "thickness": "2"
        }
      ]
    }
  ],
  "trendlines": [
    {
      "line": [
        {
          "start": "14/4/2018",
          "displayvalue": "AC Testing",
          "color": "5D5D5D",
          "thickness": "1",
          "dashed": "1"
        }
      ]
    }
  ],
  "milestones": {
    "milestone": [
      {
        "date": "30/4/2018",
        "taskid": "10-1",
        "color": "#f8bd19",
        "shape": "star",
        "tooltext": "Store Opening"
      }
    ]
  },
  "tasks": {
    "task": [
      {
        "label": "Clear Site (4 Days)",
        "processid": "1",
        "start": "1/3/2018",
        "end": "5/3/2018",
        "id": "1-1",
        "color": "#5D62B5"
      },
      {
        "label": "Drainage & Foundation (7 Days)",
        "processid": "2",
        "start": "6/3/2018",
        "end": "13/3/2018",
        "id": "2-1",
        "color": "#5D62B5"
      },
      {
        "label": "Ground Floor (8 Days)",
        "processid": "3",
        "start": "14/3/2018",
        "end": "22/3/2018",
        "id": "3-1",
        "color": "#5D62B5"
      },
      {
        "label": "First Floor (5 Days)",
        "processid": "4",
        "start": "23/3/2018",
        "end": "28/3/2018",
        "id": "4-1",
        "color": "#5D62B5"
      },
      {
        "label": "Roofing (5 Days)",
        "processid": "5",
        "start": "29/3/2018",
        "end": "3/4/2018",
        "id": "5-1",
        "color": "#5D62B5"
      },
      {
        "label": "Connect Electricity (6 Days)",
        "processid": "6",
        "start": "4/4/2018",
        "end": "10/4/2018",
        "id": "6-1",
        "color": "#5D62B5"
      },
      {
        "label": "Air Conditioning (3 Days)",
        "processid": "7",
        "start": "11/4/2018",
        "end": "14/4/2018",
        "id": "7-1",
        "color": "#5D62B5"
      },
      {
        "label": "Interiors (8 Days)",
        "processid": "8",
        "start": "15/4/2018",
        "end": "23/4/2018",
        "id": "8-1",
        "color": "#5D62B5"
      },
      {
        "label": "Racking (3 Days)",
        "processid": "9",
        "start": "24/4/2018",
        "end": "28/4/2018",
        "id": "9-1",
        "color": "#5D62B5"
      },
      {
        "label": "Stock Shelving (1 Days)",
        "processid": "10",
        "start": "29/4/2018",
        "end": "30/4/2018",
        "id": "10-1",
        "color": "#5D62B5",
        "toppadding": "9"
      }
    ]
  },
  "processes": {
    "headertext": "Task",
    "isanimated": "1",
    "headervalign": "bottom",
    "headeralign": "left",
    "align": "left",
    "isbold": "1",
    "bgalpha": "25",
    "process": [
      {
        "label": "Clear site",
        "id": "1"
      },
      {
        "label": "Drainage & Foundation",
        "id": "2"
      },
      {
        "label": "Ground Floor",
        "id": "3"
      },
      {
        "label": "First Floor",
        "id": "4"
      },
      {
        "label": "Roofing",
        "id": "5"
      },
      {
        "label": "Connect Electricity",
        "id": "6"
      },
      {
        "label": "Air Conditioning",
        "id": "7"
      },
      {
        "label": "Interiors",
        "id": "8"
      },
      {
        "label": "Racking",
        "id": "9"
      },
      {
        "label": "Stock Shelving",
        "id": "10"
      }
    ]
  },
  "categories": [
    {
      "align": "middle",
      "category": [
        {
          "start": "1/3/2018",
          "end": "31/3/2018",
          "label": "March"
        },
        {
          "start": "1/4/2018",
          "end": "1/5/2018",
          "label": "April"
        }
      ]
    },
    {
      "align": "center",
      "category": [
        {
          "start": "1/3/2018",
          "end": "7/3/2018",
          "label": "Week 1"
        },
        {
          "start": "8/3/2018",
          "end": "14/3/2018",
          "label": "Week 2"
        },
        {
          "start": "15/3/2018",
          "end": "21/3/2018",
          "label": "Week 3"
        },
        {
          "start": "22/3/2018",
          "end": "28/3/2018",
          "label": "Week 4"
        },
        {
          "start": "29/3/2018",
          "end": "5/4/2018",
          "label": "Week 5"
        },
        {
          "start": "6/4/2018",
          "end": "12/4/2018",
          "label": "Week 6"
        },
        {
          "start": "13/4/2018",
          "end": "19/4/2018",
          "label": "Week 7"
        },
        {
          "start": "19/4/2018",
          "end": "25/4/2018",
          "label": "Week 8"
        },
        {
          "start": "25/4/2018",
          "end": "1/5/2018",
          "label": "Week 9"
        }
      ]
    }
  ]
}""")
   return render(request, 'chart.html', {'output': chartObj.render()})
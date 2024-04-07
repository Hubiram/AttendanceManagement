import json
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Student, Subject, Attendance
from .forms import AttendanceForm
from datetime import datetime

def main(request): 
    return render(request, 'main.html')

def entry(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            subject_id = form.cleaned_data['subject_id']
            date_str = request.POST.get('date')
            attended = form.cleaned_data['attended']

        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

        new_attendance_id = len(data['attendance']) + 1

        data['attendance'].append({
            'id': new_attendance_id,
            'student': student_id,
            'subject': subject_id,
            'date': date_str,
            'attended': attended
        })

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return redirect('main')
    
    else:
        form = AttendanceForm()

    return render(request, 'entry.html', {'form': form})

def fetch_subject_name(subject_id):
    with open('data.json', 'r') as file:
        data = json.load(file)
        for subject in data['subjects']:
            if subject['id'] == int(subject_id):
                return subject['name']
    return None

def report(request):
    attendance_entries = None
    total_classes = None
    total_attended = None
    student_name = None

    if 'student_id' in request.GET:
        student_id = request.GET.get('student_id')
        with open('data.json', 'r') as file:
            data = json.load(file)
            for student in data['students']:
                if student['id'] == int(student_id):
                    student_name = student['name']
                    break

    if 'daily_attendance' in request.GET:
        student_id = request.GET.get('student_id')
        with open('data.json', 'r') as file:
            data = json.load(file)
        student = [student for student in data['students'] if student['id'] == int(student_id)]
        if student:
            student_name = student[0]['name']
        attendance_entries = []
        for entry in data['attendance']:
            if str(entry['student']) == student_id:
                subject_name = fetch_subject_name(entry['subject'])  # Fetch subject name
                entry['subject_name'] = subject_name
                attendance_entries.append(entry)
                
    elif 'attendance_report' in request.GET:
        subject_attendance = {}
        student_id = request.GET.get('student_id')
        with open('data.json', 'r') as file:
            data = json.load(file)
        for entry in data['attendance']:
            if str(entry['student']) == student_id:
                subject_id = entry['subject']
                subject_name = fetch_subject_name(subject_id)
                if subject_id not in subject_attendance:
                    subject_attendance[subject_id] = {'name': subject_name,'total_classes': 0, 'total_attended': 0}
                subject_attendance[subject_id]['total_classes'] += 1
                if entry['attended']:
                    subject_attendance[subject_id]['total_attended'] += 1       
        return render(request, 'report.html', {'student_name': student_name,'subject_attendance': subject_attendance})
    
    return render(request, 'report.html', {
        'student_name': student_name,
        'attendance_entries': attendance_entries,
        'total_classes': total_classes,
        'total_attended': total_attended
    })
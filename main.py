import xml.dom.minidom
import numpy as np


def main():
    '''Presenting formatted data from the timetable xml file'''

    #  !!!--> THIS DOC NAME SHOULD BE CHANGED FOR NEWER TIMETABLES (XML files) <--!!!
    doc_name = "asctt2012.xml"
    doc = xml.dom.minidom.parse(doc_name)

    # Creating dictionaries of all the data required

    # subject_dict has format : {subjectid: name}
    subject = doc.getElementsByTagName("subject")
    subject_dict = {}
    for data in subject:
        subject_dict[data.getAttribute("id")] = data.getAttribute("name")

    # days_dict has format : {days: name}
    days = doc.getElementsByTagName("daysdef")
    days_dict = {}
    for data in days:
        days_dict[data.getAttribute("days")] = data.getAttribute("name")

    # classrooms_dict has format : {classroomid: name}
    classrooms = doc.getElementsByTagName("classroom")
    classrooms_dict = {}
    for data in classrooms:
        classrooms_dict[data.getAttribute("id")] = data.getAttribute("name")

    # teacher_dict has format : {teacherid: name}
    teacher = doc.getElementsByTagName("teacher")
    teacher_dict = {}
    for data in teacher:
        teacher_dict[data.getAttribute("id")] = data.getAttribute("name")

    # class_dict has format : {classid: name}
    clas = doc.getElementsByTagName("class")
    class_dict = {}
    for data in clas:
        class_dict[data.getAttribute("id")] = data.getAttribute("name")

    # lesson_dict has format : {lessonid: [classid, subjectid, teacherid, daydefid, classroomids]}
    lesson = doc.getElementsByTagName("lesson")
    lesson_dict = {}
    for data in lesson:
        lesson_dict[data.getAttribute("id")] = [data.getAttribute(
            "classids"), data.getAttribute("subjectid"), data.getAttribute("teacherids"), data.getAttribute("daysdefid"), data.getAttribute("classroomids")]

    # card_dict has format : {cardid: [period, week, days]}
    card = doc.getElementsByTagName("card")
    card_dict = {}
    for data in card:
        card_dict[data.getAttribute("lessonid")] = [
            data.getAttribute("period"), data.getAttribute("weeks"), data.getAttribute("days")]

    # Using dicts to get required information
    req_info = []
    for key, value in lesson_dict.items():
        indv_elem = []

        # Class
        class_id = value[0]
        if ',' in class_id:
            temp = ""
            arr = value[0].split(",")
            for i in arr:
                temp += class_dict.get(i)
                if i != arr[len(arr)-1]:
                    temp += "-"
            indv_elem.append(temp)
        else:
            indv_elem.append(class_dict.get(class_id))

        # Period
        indv_elem.append(card_dict.get(key)[0])

        # Teacher name
        teacher_id = value[2]
        if ',' in teacher_id:
            temp = ""
            arr = value[2].split(",")
            for i in arr:
                temp += teacher_dict.get(i)
            indv_elem.append(temp)
        elif teacher_id == "":
            indv_elem.append("No teacher")
        else:
            indv_elem.append(teacher_dict.get(teacher_id))

        # Subject
        subject_id = value[1]
        indv_elem.append(subject_dict.get(subject_id))

        # Day
        day = card_dict.get(key)[2]
        indv_elem.append(days_dict.get(day))

        # Classroom
        classroom_id = value[4]
        if ',' in classroom_id:
            indv_elem.append("Requires manual input (Multiple classrooms)")
        elif classroom_id == "":
            indv_elem.append("No classroom")
        else:
            indv_elem.append(classrooms_dict.get(classroom_id))

        # Week
        if (card_dict.get(key)[1] == "10"):
            indv_elem.append("Odd")
        elif (card_dict.get(key)[1] == "01"):
            indv_elem.append("Even")
        elif (card_dict.get(key)[1] == ""):
            indv_elem.append("No information")
        else:
            indv_elem.append("All")

        req_info.append(indv_elem)

    req_info[0] = ["Class/Section", "Period No.",
                   "Teacher", "Subject", "Day", "Classrooom", "Week"]

    np.savetxt("REQUIRED.csv", req_info, delimiter=", ", fmt='% s')


if __name__ == "__main__":
    main()

import xml.dom.minidom
import numpy as np

def main():
    '''Presenting formatted data from the timetable xml file'''    
    
    #  !!!--> THIS DOC NAME SHOULD BE CHANGED FOR NEWER TIMETABLES (XML files) <--!!!
    doc_name = "asctt2012.xml"
    doc = xml.dom.minidom.parse(doc_name);


    # Creating dictionaries of all the data required
    
    # subject_dict has format : {subjectid: name}
    subject = doc.getElementsByTagName("subject")
    subject_dict = {}
    for data in subject:
        subject_dict[data.getAttribute("id")] = data.getAttribute("name")
    
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
   
    # lesson_dict has format : {lessonid: [classid, subjectid, teacherid]} 
    lesson = doc.getElementsByTagName("lesson")
    lesson_dict = {}
    for data in lesson:
        lesson_dict[data.getAttribute("id")] = [data.getAttribute("classids"), data.getAttribute("subjectid"), data.getAttribute("teacherids")]

    # card_dict has format : {cardid: [period, week]} 
    card = doc.getElementsByTagName("card")
    card_dict = {}
    for data in card:
        card_dict[data.getAttribute("lessonid")] = [data.getAttribute("period"), data.getAttribute("weeks")]

    # Using dicts to get required information
    req_info = [[]]
    for key, value in card_dict.items():
        indv_elem = []
        
        # Class
        class_id = lesson_dict.get(key)[0]
        indv_elem.append(class_dict.get(class_id))
        
        # Period
        indv_elem.append(value[0])
        
        # Teacher name
        teacher_id = lesson_dict.get(key)[2]
        indv_elem.append(teacher_dict.get(teacher_id))
        
        # Subject
        subject_id = lesson_dict.get(key)[1]
        indv_elem.append(subject_dict.get(subject_id))
        
        # Week
        if (value[1] == 10):
            indv_elem.append("Odd")
        elif (value[1] == 10):
            indv_elem.append("Even")
        else:
            indv_elem.append("All")
        
        req_info.append(indv_elem)
        
    
    np.savetxt("GFG.csv", req_info, delimiter = ", ", fmt ='% s')      
        
      


if __name__ == "__main__":
    main();
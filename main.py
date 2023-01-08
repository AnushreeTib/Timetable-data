import xml.dom.minidom

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


if __name__ == "__main__":
    main();
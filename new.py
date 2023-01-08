import xml.dom.minidom


def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("asctt2012.xml")

    # print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    # get a list of XML tags from the document and print each one
    subject = doc.getElementsByTagName("subject")
    subject_dict = {}
    for skill in subject:
        subject_dict[skill.getAttribute("id")] = skill.getAttribute("name")
    # print(subject_dict)

    teacher = doc.getElementsByTagName("teacher")
    teacher_dict = {}
    for skill in teacher:
        teacher_dict[skill.getAttribute("id")] = skill.getAttribute("name")
    # print(teacher_dict)

    clas = doc.getElementsByTagName("class")
    class_dict = {}
    for skill in clas:
        class_dict[skill.getAttribute("id")] = skill.getAttribute("name")
    # print(class_dict)

    lesson = doc.getElementsByTagName("lesson")
    lesson_dict = {}
    for skill in lesson:
        lesson_dict[skill.getAttribute("id")] = [skill.getAttribute(
            "classids"), skill.getAttribute("subjectid"), skill.getAttribute("teacherids")]
    # print(lesson_dict)

    card = doc.getElementsByTagName("card")
    card_dict = {}
    for skill in card:
        card_dict[skill.getAttribute("lessonid")] = [skill.getAttribute(
            "period"), skill.getAttribute("weeks")]
    # print(card_dict)

    # using dicts to get
    req_info = [[]]
    for key, value in card_dict.items():
        indv_elem = []
        # class
        class_id = lesson_dict.get(key)[0]
        indv_elem.append(class_dict.get(class_id))
        # period
        indv_elem.append(value[0])
        # teacher name
        teacher_id = lesson_dict.get(key)[2]
        indv_elem.append(teacher_dict.get(teacher_id))
        # subject
        subject_id = lesson_dict.get(key)[1]
        indv_elem.append(subject_dict.get(subject_id))
        # week
        if (value[1] == 10):
            indv_elem.append("Odd")
        elif (value[1] == 11):
            indv_elem.append("All")
        else:
            indv_elem.append("Even")
        req_info.append(indv_elem)

    for elem in req_info:
        print(elem)

    # hi this a comment
if __name__ == "__main__":
    main()

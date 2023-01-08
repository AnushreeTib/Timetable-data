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
    print(subject_dict)

    teacher = doc.getElementsByTagName("teacher")
    teacher_dict = {}
    for skill in teacher:
        teacher_dict[skill.getAttribute("id")] = skill.getAttribute("name")
    print(teacher_dict)

    clas = doc.getElementsByTagName("class")
    class_dict = {}
    for skill in clas:
        class_dict[skill.getAttribute("id")] = skill.getAttribute("name")
    print(class_dict)

    lesson = doc.getElementsByTagName("lesson")
    lesson_dict = {}
    for skill in lesson:
        lesson_dict[skill.getAttribute("id")] = [skill.getAttribute(
            "classids"), skill.getAttribute("subjectid"), skill.getAttribute("teacherids")]
    print(lesson_dict)

    card = doc.getElementsByTagName("card")
    card_dict = {}
    for skill in card:
        card_dict[skill.getAttribute("lessonid")] = [skill.getAttribute(
            "period"), skill.getAttribute("weeks")]
    print(card_dict)


if __name__ == "__main__":
    main()

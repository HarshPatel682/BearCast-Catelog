import json 

jsonData = """
[ 
    {"title": "Connection", "img": "img/connection.png", "href":"subpages/connection.html", "date": "05 Sept 2021"}, 
    {"title": "First", "img": "img/first.jpg", "href":"subpages/first.html", "date": "18 Sept 2021", "notes": "note from first date"}, 
    {"title": "Old Town", "img": "img/oldtown.jpg", "href":"subpages/oldtown.html", "date": "08 Oct 2021"}, 
    {"title": "DC Zoo", "img": "img/zoo.jpg", "href":"subpages/zoo.html", "date": "23 Oct 2021"}, 
    {"title": "Bless Up", "img": "img/blessup.jpg", "href":"subpages/blessup.html", "date": "31 Oct 2021"},
    {"title": "Cuddle", "img": "img/cuddle.jpg", "href":"subpages/cuddle.html", "date": "07 Nov 2021"},
    {"title": "Kiss", "img": "img/kiss.jpg", "href":"subpages/kiss.html", "date": "12 Nov 2021"},
    {"title": "Faint", "img": "img/faint.jpg", "href":"subpages/faint.html", "date": "27 Nov 2021"},
    {"title": "1st Visit", "img": "img/visit.jpg", "href":"subpages/visit.html", "date": "19 Dec 2021"},
    {"title": "I &#10084; U", "img": "img/loveyou.jpg", "href":"subpages/loveyou.html", "date": "06 Jan 2022"},
    {"title": "Poconos", "img": "img/poconos.jpg", "href":"subpages/poconos.html", "date": "14 Jan 2022"},
    {"title": "Nala", "img": "img/nala.jpg", "href":"subpages/nala.html", "date": "17 Jan 2022"},
    {"title": "The Boys", "img": "img/theboys.jpg", "href":"subpages/theboys.html", "date": "13 Feb 2022"},
    {"title": "Work Trip", "img": "img/worktrip.jpg", "href":"subpages/worktrip.html", "date": "15 Apr 2022"},
    {"title": "Gru &#58149; RT", "img": "img/grurtengagement.jpg", "href":"subpages/grurtengagement.html", "date": "16 Apr 2022"},
    {"title": "Parent Meet", "img": "img/parentsmeeting.jpg", "href":"subpages/parentsmeeting.html", "date": "06 May 2022"},
    {"title": "Marriage", "img": "img/marriage.jpg", "href":"subpages/marriage.html", "date": "12 May 2022"},
    {"title": "San Diego", "img": "img/sandiego.jpg", "href":"subpages/sandiego.html", "date": "19 May 2022"},
    {"title": "Raj's Wedding", "img": "img/rajwedding.jpg", "href":"subpages/rajwedding.html", "date": "08 Jun 2022"},
    {"title": "S+D Engagement", "img": "img/sdengagement.jpg", "href":"subpages/sdengagement.html", "date": "18 Jun 2022"},
    {"title": "Reecha San Diego", "img": "img/reechasandiego.jpg", "href":"subpages/rsandiego.html", "date": "10 Jul 2022"},
    {"title": "Parth Engagement", "img": "img/parthengagement.jpg", "href":"subpages/parthengagement.html", "date": "21 Aug 2022"},
    {"title": "Orlando", "img": "img/orlando.jpg", "href":"subpages/orlando.html", "date": "21 Sept 2022"},
    {"title": "RH Engagement", "img": "img/24_rhengagement.jpg", "href":"subpages/rhengagement.html", "date": "08 Oct 2022"}
] 
"""

# Convert JSON data to a Python object 
data = json.loads(jsonData) 
  
# Iterate through the JSON array 
for item in data: 
    print('<div class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12 mb-5">')
    print('<figure class="effect-ming tm-video-item">')
    print('<img src="' + item["img"] +'" alt="Image" class="img-fluid">')
    print('<figcaption class="d-flex align-items-center justify-content-center">')
    print('<h2>' + item["title"] + '</h2>')
    print('<a href="' + item["href"] + '">View more</a>')
    print('</figcaption>')
    print('</figure>')
    print('<div class="d-flex justify-content-between tm-text-gray">')
    print('<span class="tm-text-gray-light">' + item["date"] + '</span>')
    print('</div>')
    print('</div>')

    # print('cat subpages/connection.html > ' + item["href"])
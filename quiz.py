#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value #sets the values for each element to its value\
$
    return d
d = FStoD() #global dictionary


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ========
print "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!!
print '<html><head> <link rel = "stylesheet" href="quiz.css"> <title> what you are! </title></head>\n'
print '<body style="background-image:url(socialmedia.jpg)">'
print '<div class = "text">'
# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
print "<br><center><h1>YOU SHOULD TRY </h1></center>"

def tag(t1,t2,string):
    return t1+string+t2

def statement(L):
    end = "<br> <h2 align = center>"
    for x in L:
        end += x + " and "
    end = end[:-5]
    end += "!"
    return end + "</h2><br>"

def quizzer():

    answers = {}
    answers['Facebook and Google+'] = 0
    answers['LinkedIn and PinInterest'] = 0
    answers['Instagram and Flickr'] = 0
    answers['Reddit and Youtube'] = 0
    answers['Twitter and Tumblr'] = 0

    if d['q1'] == 'a':
        answers['Facebook and Google+'] += 1
    if d['q1'] == 'b':
        answers['LinkedIn and PinInterest'] += 1
    if d['q1'] == 'c':
        answers['Instagram and Flickr'] += 1
    if d['q1'] == 'd':
        answers['Reddit and Youtube'] += 1
    if d['q1'] == 'e':
        answers['Twitter and Tumblr'] += 1

    if d['q2'] == 'a':
        answers['Reddit and Youtube'] += 1
        answers['LinkedIn and PinInterest'] += 1
    if d['q2'] == 'b':
        answers['Instagram and Flickr'] += 1
    if d['q2'] == 'c':
        answers['Facebook and Google+'] += 1
        answers['Twitter and Tumblr'] += 1

    if d['q3'] == 'a':
        answers['Twitter and Tumblr'] += 1
    if d['q3'] == 'b':
        answers['Instagram and Flickr'] += 1
    if d['q3'] == 'c':
        answers['Facebook and Google+'] += 1
    if d['q3'] == 'd':
        answers['LinkedIn and PinInterest'] += 1
    if d['q3'] == 'e':
        answers['Reddit and Youtube'] += 1

    if d['q4'] == 'a':
        answers['LinkedIn and PinInterest'] += 1
        answers['Reddit and Youtube'] += 1
    if d['q4'] == 'b':
        answers['Twitter and Tumblr'] += 1
        answers['Instagram and Flickr'] += 1
        answers['Facebook and Google+'] += 1

    if d['q5'] == 'a':
        answers['Instagram and Flickr'] += 1
    if d['q5'] == 'b':
        answers['LinkedIn and PinInterest'] += 1
    if d['q5'] == 'c':
        answers['Facebook and Google+'] += 1
    if d['q5'] == 'd':
        answers['Twitter and Tumblr'] += 1
    if d['q5'] == 'e':
        answers['Reddit and Youtube'] += 1

    if d['q6'] == 'a':
        answers['Instagram and Flickr'] += 1
        answers['LinkedIn and PinInterest'] += 1
    if d['q6'] == 'b':
        answers['Facebook and Google+'] += 1
        answers['Reddit and Youtube'] += 1
    if d['q6'] == 'c':
       answers['Twitter and Tumblr'] += 1

    if d['q7'] == 'a':
        answers['Facebook and Google+'] += 2
    if d['q7'] == 'b':
        answers['LinkedIn and PinInterest'] += 2
    if d['q7'] == 'c':
        answers['Instagram and Flickr'] += 2
    if d['q7'] == 'd':
        answers['Reddit and Youtube'] += 2
    if d['q7'] == 'e':
        answers['Twitter and Tumblr'] += 2


    maxvalue = max(answers.values())
    ans = []
    for x in answers:
        if answers[x] == maxvalue:
            ans += [x]
    print statement(ans)
    return ans

a = quizzer()

def description ():
    x = "<h3>"
    if 'Facebook and Google+' in a:
    x += '''
        You should try Facebook or Google+!  You like to talk to others and keep\
        up-to-date on the latest news.  You have instant access to BuzzFeed, \
        Bright Side and Tasty. You like to use LOL or LMAO or LEMOW.
        '''
    if 'LinkedIn and PinInterest' in a:
    x += '''
        You should try LinkedIn and PinInterest! You prefer to keep it professional\
        and won't let yourself get too distracted online, okay maybe a litle but not\
        as much as those Tumblr people.
        '''
    if 'Instagram and Flickr' in a:
    x += '''
        You should try Instagram and Flickr! You like to take pictures and document\
        your memories.  You also like to hang out with people and aren't afraid to\
        comment on a picture asking why someone didn't invite you. TFTI.
        '''
    if 'Reddit and Youtube' in a:
    x +='''
        You should try Reddit and Youtube. The sass is real with this one.  But you \
        like to reach out to people and comment advice or flames.  You're not afraid \
        to speak your mind and people like that about you.
        '''
    return x + "</h3>"

    if 'Twitter and Tumblr' in a:
    x +='''
        You should try Twitter and Tumblr. YOU ARE SO EXCITED and like to have deep \
        conversations.  You understand people and know that everything isn't always \
        what it seems. You're often short and sweet to support others. #yes.
        '''
    return x + "</h3>"

print description()
print '''
    <br><br> <h3> If you're ever in danger of anxiety attacks, get help immediately.  Check out our advice page asap! \
    <a href = "ReachOut.html">Reach Out</a></h3>
    '''
print "</div></html></center></body>"

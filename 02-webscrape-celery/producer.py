
urls = []
with open(file, 'r') as f:
    urls = f.read().splitlines()


urls = []
urls = df['url'].tolist()
url = 'amqp://gotem:gotem1234@35.185.79.116:5762/gvhost'

params.socket_timeout = 5
params = pika.URLParameters(url)


app = Celery('tasks', broker='amqp://gadmin:gotem1234@amqp://gotem:gotem1234@35.185.79.116:5762/gvhost')

#   using docker for both broker and backend
#   docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:management
#   docker pull redis

url = r'http://www.blackrock.com'

def produce():
    try:
        scrape.delay(str(url))
        print(("* Submitted: [{}]".format(url)))
    except:
        print(("ERROR ", url))

produce()

#####################

#   urls.txt    #  example

    #
    #http://www.blackrock.com
    #http://www.fidelity.com
    #http://www.nbim.no
    #http://www.troweprice.com
    #http://www.wellington.com
    #http://www.northerntrust.com
    #http://www.mfs.com
    #http://www.jpmorganfunds.com
    #http://www.us.dimensional.com
    #http://www.lgim.com
    #http://www.tiaa-cref.org
    #http://www.invesco.com
    #http://www.mcm.com
    #http://www.geodecapital.com
    #http://www.columbiamanagement.com
    #http://www.dodgeandcox.com
    #http://www.oppenheimerfunds.com
    #http://www.alliancebernstein.com
    #http://www.apg.nl
    #http://www.franklintempleton.com
    #http://www.jennison.com
    #http://www.gsam.com

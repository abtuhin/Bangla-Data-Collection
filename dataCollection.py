import urllib.request
import simplejson
#import socket


#all crawl
#bipasha hayat37297699653
#mousumiactor
#SabilaNurOfficialFanPage
#peyabipashamodel
#289400121215264
#ahona.md
#Orchita.Sporshia
#badhon.19
#milaislm
#Jacquelinemithila.bd
#bobyactor
#artist.nailanayem
#MahiyaMahiActress
#Shakib.Al.Hasan
#originalneta
#nusraatfariaofficial
#pori.monii

access_token_user = "CAACEdEose0cBABu6ImB3TvDgIKqTro6V2UxXNZCFdBeLa9gdPuu0rZAC0hTEXuYY1zXYmJrJBgmx8MxuxIP7qKGKxOr5HIuuNrXTvoZBavarcrScnxDJZARHMgvyzzGRi0dziqV29l6ZAiRAC9VaMBv2nbH4bz670ZBb0BTr8lhM5GJzcsZBafryLdZCvYMUZB5ZAgwMc90D39b3V0YXWHVLos"

url = "https://graph.facebook.com/pori.monii/posts?limit=50&access_token="+access_token_user

#socket.setdefaulttimeout(100)

res = urllib.request.urlopen(url)

json_data = simplejson.load(res)
# print(json_data)

fw = open("models.txt","w",encoding="utf8")


for i in json_data["data"]:
    print("\npost_id: "+i["id"]+"\nuser_name:"+ i["from"]["name"]+"\tid_user: "+i["from"]["id"])
    fw.write("post_id: "+i["id"]+"\nuser_name: "+i["from"]["name"]+"\tid_user: "+i["from"]["id"])

    try:
        print("post_share: "+(str(i["shares"]["count"])))
        fw.write("\npost_share: "+(str(i["shares"]["count"])))
    except KeyError: pass

    print("\npost: ")
    print(i.get("message"))

    fw.write("\npost: ")
    fw.write(str(i.get("message")))

    # print("likes: ")
    #
    # try:
    #     for j in i["likes"]["data"]:
    #         print("liker_id: "+j["id"]+"\tliker_name: "+j["name"])
    #     paging = i["likes"]["paging"]["next"]
    #     while(paging is not "null"):
    #         res = urllib.request.urlopen(paging)
    #         more_data = simplejson.load(res)
    #         for a in more_data["data"]:
    #             print("liker_id: "+a["id"]+"\tliker_name: "+a["name"])
    #         paging = more_data["paging"]["next"]
    #
    # except KeyError: pass

    try:
        for k in i["comments"]["data"]:
            print("commenter_id: "+k["from"]["id"]+"\tcommenter_name: "+k["from"]["name"]+"\tcomment_liker: "+str(k["like_count"]))
            print("comment: "+k["message"])
            fw.write("\ncommenter_id: "+k["from"]["id"]+"\tcommenter_name: "+k["from"]["name"]+"\tcomment_liker: "+str(k["like_count"]))
            fw.write("\ncomment: "+k["message"])
        paging = i["comments"]["paging"]["next"]
        while(paging is not "null"):
            res = urllib.request.urlopen(paging)
            more_data = simplejson.load(res)
            for a in more_data["data"]:
                print("commenter_id: "+a["from"]["id"]+"\tcommenter_name: "+a["from"]["name"]+"\tcomment_liker: "+str(a["like_count"]))
                print("comment: "+a["message"])
                fw.write("\ncommenter_id: "+a["from"]["id"]+"\tcommenter_name: "+a["from"]["name"]+"\tcomment_liker: "+str(a["like_count"]))
                fw.write("\ncomment: "+a["message"])
            paging = more_data["paging"]["next"]

    except KeyError: pass


paging = json_data["paging"]["next"]

while(paging):
    res = urllib.request.urlopen(paging)
    json_data = simplejson.load(res)

    try:
        if("paging" not in json_data):
            break

        for i in json_data["data"]:
            print("\npost_id: "+i["id"]+"\nuser_name:"+ i["from"]["name"]+"\tid_user: "+i["from"]["id"])
            fw.write("\npost_id: "+i["id"]+"\nuser_name: "+i["from"]["name"]+"\tid_user: "+i["from"]["id"])

            try:
                print("post_share: "+(str(i["shares"]["count"])))
                fw.write("\npost_share: "+(str(i["shares"]["count"])))
            except KeyError: pass

            print("\npost: ")
            print(i.get("message"))

            fw.write("\npost: ")
            fw.write(str(i.get("message")))

            # print("likes: ")
            #
            # try:
            #     for j in i["likes"]["data"]:
            #         print("liker_id: "+j["id"]+"\tliker_name: "+j["name"])
            #     paging = i["likes"]["paging"]["next"]
            #     while(paging is not "null"):
            #         res = urllib.request.urlopen(paging)
            #         more_data = simplejson.load(res)
            #         for a in more_data["data"]:
            #             print("liker_id: "+a["id"]+"\tliker_name: "+a["name"])
            #         paging = more_data["paging"]["next"]
            #
            # except KeyError: pass

            try:
                for k in i["comments"]["data"]:
                    print("commenter_id: "+k["from"]["id"]+"\tcommenter_name: "+k["from"]["name"]+"\tcomment_liker: "+str(k["like_count"]))
                    print("comment: "+k["message"])
                    fw.write("\ncommenter_id: "+k["from"]["id"]+"\tcommenter_name: "+k["from"]["name"]+"\tcomment_liker: "+str(k["like_count"]))
                    fw.write("\ncomment: "+k["message"])
                paging = i["comments"]["paging"]["next"]
                while(paging is not "null"):
                    res = urllib.request.urlopen(paging)
                    more_data = simplejson.load(res)
                    for a in more_data["data"]:
                        print("commenter_id: "+a["from"]["id"]+"\tcommenter_name: "+a["from"]["name"]+"\tcomment_liker: "+str(a["like_count"]))
                        print("comment: "+a["message"])
                        fw.write("\ncommenter_id: "+a["from"]["id"]+"\tcommenter_name: "+a["from"]["name"]+"\tcomment_liker: "+str(a["like_count"]))
                        fw.write("\ncomment: "+a["message"])
                    paging = more_data["paging"]["next"]

            except KeyError: pass
        paging = json_data["paging"]["next"]

    except KeyError:pass
fw.write("\n\n")

fw.close()


import json
import time


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
           return json.load(file)
    except FileNotFoundError as e :  
        return [] 


def helper(video):
 with open('youtube.txt',"w") as  file:
     json.dump(video, file)
     
     
def  list_videos(videos):
  
  for i,v in  enumerate(videos,start=1):
      print(f"{i} : {v['name']},{v['time']}") 

def add_video(videos):
    name=input("enter video name")
    time=input("Enter video time:")
    videos.append({'name':name,'time':time})
    helper(videos)

def update_video(videos):
    list_videos(videos)
    num=int(input("Enter video number"))
    if 1<=num<=len(videos):
          name=input("enter video name")
          time=input("Enter video time:")
          videos[num-1]={'name':name,'time':time}
          helper(videos)
    else:
        print("invalid input")      
   
    

def delete_video(videos):
    list_videos(videos)
    num=int(input("enter the number"))
    if 1<=num<=len(videos):
         del videos[num-1]
         helper(videos)
    else:
        print("invalid input")  

def main():
    videos=load_data()
    while True:
        print('\n  yt manger\n')
        print("1 list all the yt videos\n")
        print("2 add a yt videos\n")
        print("3 update the  yt videos\n")
        print("4 delete  the yt videos\n")
        print("5  Exit \n")
        choice = str(input("Enter your choice: "))
        match choice:
            case '1':
                     list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == '__main__':
    main()

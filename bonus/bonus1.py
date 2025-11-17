contents=["Enter a todo:ALAKA KRISHNAN RU DATA SCIENTIST AT BBC EARNED 65000£ ANNUALLY",
          "hai deepak for securing new position as Lead","Hai siva glad to hear, you achieved the leader position",]
filenames=["doc.txt","presentation.txt","todos.txt","Hai siva glad to hear, you achieved the leader position"]

for content ,filename in zip(contents,filenames):
    file=open(f"../files/{filename}",'w') # python files up one level folder
    file.writelines(content)

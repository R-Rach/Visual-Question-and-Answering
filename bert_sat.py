import sys
sys.path.insert(0, './sat_final')
sys.path.insert(0, './BERT')

from sat_final.caption import *
from BERT.bert import QA

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image 


if __name__ == '__main__':

	model = QA('/complete_path_to_BERT_model_with_model_file_name/')

	root=Tk()
	root.geometry('750x750')
	root.title('BERT-Show Attend and Tell')

	def browsefunc():
		global img_path
		filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		print('filename--------- ',filename)
		img_path=filename
		try:
			print(img_path)
			pathlabel.config(text='Image selected -> '+filename)

			img = Image.open(filename)
			img = img.resize((500,400), Image.ANTIALIAS)
			img = ImageTk.PhotoImage(img)     
			panel.config(image = img)
			panel.image = img

		except:
			print("error")
			pathlabel.config(text='Error selecting Image')	

	def get_ans():
		caption = sat_caption(img_path)
		# print('==>',caption)
		contextl.config(text='Generated Caption: '+caption)

		ques = qentry.get("1.0",'end-1c')

		answer = model.predict(caption,ques)
		# print(answer['answer'])
		answer = answer['answer']
		ansL.config(text="Answer: "+answer)

	def quit():
		root.destroy()


	empty=Label(root,text='                               ')
	empty.pack()
	
	qlabel=Label(root, text='Enter your Question')
	qlabel.pack()
	
	qentry=Text(root,height=3,width=60)
	qentry.pack(ipady=3)
	
	empty2=Label(root,text='                               ')
	empty2.pack()
	
	browsebutton = Button(root, text="Browse", command=browsefunc)
	browsebutton.pack()
	
	pathlabel = Label(root, text='Image not selected')
	pathlabel.pack()
	
	panel = Label(root)
	panel.pack()
	
	empty3=Label(root,text='                               ')
	empty3.pack()
	
	getansbtn=Button(root, text="Get Answer", command=get_ans)
	getansbtn.pack()
	
	contextl=Label(root, text='Generated Caption: ')
	contextl.pack()
	
	ansL=Label(root, text="Answer: ")
	ansL.pack()
	
	empty=Label(root,text='                               ')
	empty.pack()
	
	quitbtn=Button(root,text="Quit",command=quit)
	quitbtn.pack()
	
	root.mainloop()

	
	# image_path = '/home/abc/SAT/MAIN/sat_final/test/3.jpg'

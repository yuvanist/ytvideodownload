'''
	Author: DG
'''
from pytube import YouTube

def url_from_user():
	url = input()
	return url

def filter_only_mp4(obj):
	return obj.streams.filter(file_extension='mp4',progressive=True).order_by('resolution').desc()

def kilo_to_mega_bytes(filesize_in_kb):
	inmb = filesize_in_kb/(1024*1024)
	return str(inmb)+' '+'MB'

def display_resolutions(obj_with_only_mp4):
	res_list = []
	for i in obj_with_only_mp4:
		res = i.resolution
		filesize_in_kb = obj_with_only_mp4.get_by_resolution(res).filesize
		filesize_in_mb = kilo_to_mega_bytes(filesize_in_kb)
		res_list.append([res,filesize_in_mb])
	cnt = 1
	print('ID RESOLUTION SIZE IN MB')
	for i in res_list:
		temp=str(cnt)+'   '+str(i[0])+'       '+str(i[1])
		print(temp)
		cnt+=1
	return res_list


def main():
	print("Author: DG")
	print('http://github.com/yuvanist')
	print('-'*30)
	print('This script takes youtube URL as input and donwlods the video for you')
	print('-'*30)
	print('Enter the youtube URL you want to download')
	url = url_from_user()
	obj = YouTube(url)
	print()
	print('Title of the YouTube video =',obj.title)
	print('Available resolution for the video')
	obj_with_only_mp4 = filter_only_mp4(obj)
	res_list = display_resolutions(obj_with_only_mp4)
	#print(res_list)
	print('Enter resolution ID you want to download')
	res_id =  int(input())
	try:
		final = obj_with_only_mp4.get_by_resolution(res_list[res_id-1][0])
		final.download()
	except:
		print('Please enter valid resolution ID')
	print('Downloaded successfully. Please check current directory! :)')


if __name__ == '__main__':
	main()

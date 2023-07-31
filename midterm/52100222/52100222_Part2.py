import cv2
import numpy as np
from matplotlib import pyplot as plt
# thêm các thư viện numpy, opencv, module pyplot từ matplotlib

img = cv2.imread("demo.jpg", 0) #import ảnh sau đó chuyển sang xám
#tạo biến img lưu hình ảnh demo.jpg
def compute_hist(img):  #Hàm tính histogram của ảnh
    hist = np.zeros((256,), np.uint8) # tạo một hist cho ảnh
    h, w = img.shape[:2] # lưu chiều cao và rộng của ảnh
    for i in range(h): # duyệt chiều cao
        for j in range(w): # duyệt chiều rộng
            hist[img[i][j]] += 1 #đây là điểm ảnh của ảnh 
    return hist # trả về tập điểm ảnh của ảnh

def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64) # tạo một mảng comulator có độ dài bằng độ dài mảng điểm ảnh
    for i in range(len(cumulator)): #Duyệt tất cả các điểm ảnh
        cumulator[i] = hist[:i].sum() #Lưu tổng các điểm ảnh
    print(cumulator)#in ra các điểm ảnh
    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255 #Kéo giãn cac điểm ảnh ra
    new_hist = np.uint8(new_hist)
    return new_hist

hist = compute_hist(img).ravel() # trả về hist một danh sách điểm ảnh
new_hist = equal_hist(hist)#cân bằng histogram

h, w = img.shape[:2] #set chiều cao và rộng cho ảnh
for i in range(h):
   for j in range(w):
       img[i,j] = new_hist[img[i,j]] #gán điểm ảnh mới đã qua xử lý vào điểm ảnh cũ
       
fig = plt.figure()
ax = plt.subplot(121)
plt.imshow(img, cmap='gray') #chỉnh ảnh xám

plt.subplot(122)
plt.plot(img)
plt.show()


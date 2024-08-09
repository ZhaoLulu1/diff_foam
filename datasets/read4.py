import pickle
import matplotlib.pyplot as plt
import math
import numpy as np

# 1. 从 .pkl 文件中加载数据
with open('rosbag2_2024_08_01-16_54_08.pkl', 'rb') as file:
    data = pickle.load(file)

# 2. 获取图像数据
images = data.get('image', [])

def convert_bgr_to_rgb(image):
    """将 BGR 图像转换为 RGB 图像"""
    if image.ndim == 3 and image.shape[2] == 3:
        return image[:, :, ::-1]
    return image

def display_images(images, page, images_per_page=40):
    num_images = len(images)
    num_cols = 10  # 每行显示的图像数量
    num_rows = math.ceil(images_per_page / num_cols)  # 每页的行数
    start_idx = page * images_per_page
    end_idx = min(start_idx + images_per_page, num_images)
    
    # 创建一个绘图窗口，调整子图的数量和大小
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(40, 5 * num_rows))
    
    for i in range(num_rows):
        for j in range(num_cols):
            index = start_idx + i * num_cols + j
            if index < end_idx:
                image_rgb = convert_bgr_to_rgb(images[index])
                axes[i, j].imshow(image_rgb)
                axes[i, j].axis('off')
                axes[i, j].set_title(f'Image {index+1}')
            else:
                axes[i, j].axis('off')  # 隐藏多余的子图框架
    
    plt.tight_layout()
    plt.show()

# 3. 分页显示图像
if isinstance(images, list) and len(images) > 0:
    num_images = len(images)
    images_per_page = 40  # 每页显示的图像数量
    num_pages = math.ceil(num_images / images_per_page)
    
    print(f"总共有 {num_images} 张图像，每页显示 {images_per_page} 张，共 {num_pages} 页。")
    
    page = 0
    while True:
        display_images(images, page, images_per_page)
        user_input = input(f"当前为第 {page+1}/{num_pages} 页。输入页码以查看其他页面（输入 q 退出）：")
        
        if user_input.lower() == 'q':
            break
        elif user_input.isdigit():
            page = int(user_input) - 1
            if page < 0 or page >= num_pages:
                print(f"页码无效，请输入 1 到 {num_pages} 之间的数字。")
                page = 0
        else:
            print("无效输入，请输入页码或 'q' 退出。")
else:
    print("图像数据格式不符合预期或为空")


# import pickle
# import matplotlib.pyplot as plt
# import math
# import numpy as np

# # 1. 从 .pkl 文件中加载数据
# with open('70.pkl', 'rb') as file:
#     data = pickle.load(file)

# # 2. 获取图像数据
# images = data.get('inHandImg', [])
# images = data.get('externalImg', [])

# def convert_bgr_to_rgb(image):
#     """将 BGR 图像转换为 RGB 图像"""
#     if image.ndim == 3 and image.shape[2] == 3:
#         return image[:, :, ::-1]
#     return image

# def display_images(images, page, images_per_page=40):
#     num_images = len(images)
#     num_cols = 10  # 每行显示的图像数量
#     num_rows = math.ceil(images_per_page / num_cols)  # 每页的行数
#     start_idx = page * images_per_page
#     end_idx = min(start_idx + images_per_page, num_images)
    
#     # 创建一个绘图窗口，调整子图的数量和大小
#     fig, axes = plt.subplots(num_rows, num_cols, figsize=(40, 5 * num_rows))
    
#     for i in range(num_rows):
#         for j in range(num_cols):
#             index = start_idx + i * num_cols + j
#             if index < end_idx:
#                 image_rgb = convert_bgr_to_rgb(images[index])
#                 axes[i, j].imshow(image_rgb)
#                 axes[i, j].axis('off')
#                 axes[i, j].set_title(f'Image {index+1}')
#             else:
#                 axes[i, j].axis('off')  # 隐藏多余的子图框架
    
#     plt.tight_layout()
#     plt.show()

# # 3. 分页显示图像
# if isinstance(images, list) and len(images) > 0:
#     num_images = len(images)
#     images_per_page = 40  # 每页显示的图像数量
#     num_pages = math.ceil(num_images / images_per_page)
    
#     print(f"总共有 {num_images} 张图像，每页显示 {images_per_page} 张，共 {num_pages} 页。")
    
#     page = 0
#     while True:
#         display_images(images, page, images_per_page)
#         user_input = input(f"当前为第 {page+1}/{num_pages} 页。输入页码以查看其他页面（输入 q 退出）：")
        
#         if user_input.lower() == 'q':
#             break
#         elif user_input.isdigit():
#             page = int(user_input) - 1
#             if page < 0 or page >= num_pages:
#                 print(f"页码无效，请输入 1 到 {num_pages} 之间的数字。")
#                 page = 0
#         else:
#             print("无效输入，请输入页码或 'q' 退出。")
# else:
#     print("图像数据格式不符合预期或为空")

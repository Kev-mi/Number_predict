own_pred = loaded_model.predict(img_to_test)

print(own_pred[0])

img = cv2.imread('test_2.png', 0)
plt.imshow(img, cmap='gray')

print(img.shape)
#resized_image = cv2.resize(img, (28, 28))
imageprep_2 = cv2.resize(img, (28, 28), interpolation = cv2.INTER_LINEAR)
imageprep_2 = cv2.bitwise_not(imageprep_2)

plt.imshow(imageprep_2, cmap = "gray")

print("Image's shape: {}".format(imageprep_2.shape))

img_to_test = np.reshape(imageprep_2, (1, 28*28))

print("Image's shape: {}".format(img_to_test.shape))

own_pred = loaded_model.predict(img_to_test)
print(own_pred[0])
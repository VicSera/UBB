import urllib.request

if __name__ == '__main__':
    for i in range(20):
        print("Male - " + str(i))
        urllib.request.urlretrieve("https://fakeface.rest/face/view?gender=male", "dataset-test/male/male-" + str(i) + ".jpg")
    for i in range(20):
        print("Female - " + str(i))
        urllib.request.urlretrieve("https://fakeface.rest/face/view?gender=female", "dataset-test/female/female-" + str(i) + ".jpg")
    for i in range(20):
        print("Nonhuman - " + str(i))
        urllib.request.urlretrieve("https://picsum.photos/200", "dataset-test/nonhuman/nonhuman-" + str(i) + ".jpg")
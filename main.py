from integrations.s3 import list_buckets, download_object, list_objects


def main():
    # list_buckets()
    download_object("curso-spring-ionic-higor", "cat2.jpg", "cat_new.jpg")
    # list_objects("curso-spring-ionic-higor")


if __name__ == '__main__':
    main()

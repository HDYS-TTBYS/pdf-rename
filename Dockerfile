FROM ubuntu:20.04

RUN apt-get update

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get install wget tesseract-ocr libtesseract-dev libleptonica-dev pkg-config poppler-utils tesseract-ocr-jpn tesseract-ocr-jpn-vert -y

RUN apt-get install python3-pip -y

RUN pip install tesserocr pdf2image pyocr

RUN wget -P /usr/share/tesseract-ocr/4.00/tessdata/ https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn.traineddata
RUN wget -P /usr/share/tesseract-ocr/4.00/tessdata/ https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn_vert.traineddata

RUN CPPFLAGS=-I/usr/local/include pip install tesserocr

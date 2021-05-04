#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[]) {
    // Mat src = imread(argc>1?argv[1]:"./resources/tiger.jpeg");
    // if(src.empty() ) {
    //     cerr<<"imread failed"<<endl;
    //     return -1;
    // }
    Mat src = Mat::zeros(Size(400, 400), CV_8UC3);
    circle(src, Point(200, 200), 150, Scalar(0, 0, 255), -1);
    circle(src, Point(200, 200), 100, Scalar(0, 255, 0), -1);
    circle(src, Point(200, 200), 50, Scalar(255, 0, 0), -1);
    imshow("src", src);

    Mat background = Mat::zeros(Size(src.cols, src.rows), CV_8UC3);
    rectangle(background, Point(0, 0), Point(src.cols/2, src.rows/2), Scalar(255, 0, 0), -1);
    rectangle(background, Point(src.cols/2, 0), Point(src.cols, src.rows/2), Scalar(0, 255, 0), -1);
    rectangle(background, Point(0, src.rows/2), Point(src.cols/2, src.rows), Scalar(0, 0, 255), -1);
    rectangle(background, Point(src.cols/2, src.rows/2), Point(src.cols, src.rows), Scalar(255, 255, 255), -1);
    imshow("background", background);


    Mat bit_and;
    bitwise_and(src, background, bit_and);
    imshow("bit_and", bit_and);

    Mat bit_or;
    bitwise_or(src, background, bit_or);
    imshow("bit_or", bit_or);
    
    Mat bit_xor;
    bitwise_xor(src, background, bit_xor);
    imshow("bit_xor", bit_xor);

    Mat bit_not;
    bitwise_not(src, bit_not);
    imshow("bit_not", bit_not);

//    Mat bit_and_mask;
//    Mat mask(src.rows/2, src.cols,CV_8UC3,Scalar(0, 255, 255));
//    Mat mask2(src.rows/2, src.cols,CV_8UC1);
//    bitwise_and(bit_and, bit_and, bit_and_mask, mask2);
//    imshow("bit_and_mask", bit_and_mask);
//    imshow("mask", mask);

    waitKey(0);
    destroyAllWindows();
    return 0;
}

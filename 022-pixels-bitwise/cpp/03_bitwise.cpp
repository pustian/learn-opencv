#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[]) {
    Mat src = imread(argc>1?argv[1]:"./resources/tiger.jpeg");
    if(src.empty() ) {
        cerr<<"imread failed"<<endl;
        return -1;
    }
    imshow("src", src);
    
    Mat head_roi_mask(src.rows,src.cols,CV_8UC3,Scalar(0,0,0));
    // 90:250,310:490
    rectangle(head_roi_mask, Point(310, 90), Point(490, 250), Scalar(255,255,255), -1);
    imshow("head_roi_mask", head_roi_mask);

    Mat bit_and;
    bitwise_and(src, head_roi_mask, bit_and);
    imshow("bit_and", bit_and);

    Mat bit_or;
    bitwise_or(src, head_roi_mask, bit_or);
    imshow("bit_or", bit_or);
    
    Mat bit_xor;
    bitwise_or(src, head_roi_mask, bit_xor);
    imshow("bit_xor", bit_xor);

    Mat bit_and_not;
    bitwise_not(bit_and, bit_and_not);
    imshow("bit_and_not", bit_and_not);

    waitKey(0);
    destroyAllWindows();
    return 0;
}

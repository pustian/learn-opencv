#include<opencv2/opencv.hpp>
#include<iostream>

int main(int argc, char* argv[]) {
    cv::Mat src = cv::imread(argc>1?argv[1]:"./resources/tiger.jpeg");
    if(src.empty() ) {
        std::cerr<<"imread failed"<<std::endl;
		return -1;
	}
    std::cout<<"width/cols="<<src.cols
		<<" height/rows="<<src.rows
		<<" channels="<<src.channels()
		<<std::endl;

    cv::imshow("src", src);

    int x1 = src.cols/4, x2=src.cols/2;
    int y1 = src.rows/4, y2=src.rows/2;
    cv::Mat roiImg = cv::Mat::zeros(cv::Size(x2-x1, y2-y1), CV_8UC3 );

    for(int y=0, row=y1; row<y2&& y+y1< y2; row++, y++) {
        for(int x=0, col=x1; col<x2 && x+x1 < x2; col++, x++) {
            roiImg.at<cv::Vec3b>(y, x)[0] = src.at<cv::Vec3b>(row, col)[0];
            roiImg.at<cv::Vec3b>(y, x)[1] = src.at<cv::Vec3b>(row, col)[1];
            roiImg.at<cv::Vec3b>(y, x)[2] = src.at<cv::Vec3b>(row, col)[2];
        }
    }
    std::cout<<"width/cols="<<roiImg.cols
		<<" height/rows="<<roiImg.rows
		<<" channels="<<roiImg.channels()
		<<std::endl;
    
    cv::imshow("roi", roiImg);

    cv::waitKey(0);
    cv::destroyAllWindows();
    return 0;
}

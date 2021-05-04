#include<opencv2/opencv.hpp>
#include<iostream>

int main(int argc, char* argv[]) { 
	cv::Mat src = cv::imread(argc>1?argv[1]:"./resources/tiger.jpeg");
    if(src.empty() ) {
        std::cout<<"Failed to open file"<<std::endl;
		return -1;
    }
    
	cv::imshow("src", src);

	cv::Mat gray;
	cv::cvtColor(src, gray, cv::COLOR_BGR2GRAY);
	cv::imshow("gray", gray);

	cv::Mat rev;
	cv::cvtColor(gray, rev, cv::COLOR_GRAY2BGR);
	cv::imshow("rev", rev);

	cv::waitKey(0);
	cv::destroyAllWindows();
	return 0;
}


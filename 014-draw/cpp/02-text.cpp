#include<opencv2/opencv.hpp>
#include<iostream>

int main() {
	cv::Mat background = cv::Mat::zeros(cv::Size(600, 400), CV_8UC3);
	
	std::cout<<"width/cols="<<background.cols
		<<" height/rows="<<background.rows
		<<" channels="<<background.channels()
		<<std::endl;

	cv::line(background, cv::Point(10,10), cv::Point(10, 390), cv::Scalar(0, 255, 0) );
	cv::line(background, cv::Point(10,10), cv::Point(590, 10), cv::Scalar(255, 255, 255) );
    
    std::string str = "hello opencv";
    cv::putText(background, str, cv::Point(0, 380), cv::FONT_ITALIC, 0.5, cv::Scalar(255, 255, 255), 1);

	cv::imshow("background", background);

	cv::waitKey(0);
	cv::destroyAllWindows();
    return 0;
}


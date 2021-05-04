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

	cv::circle(background, cv::Point(100,100), 50, cv::Scalar(0, 0, 255) );

	cv::rectangle(background, cv::Point(100,100), cv::Point(250, 250), cv::Scalar(255, 0, 0) );


	cv::imshow("background", background);

	cv::waitKey(0);
	cv::destroyAllWindows();
    return 0;
}


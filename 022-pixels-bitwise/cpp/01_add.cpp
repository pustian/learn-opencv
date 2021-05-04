#include<iostream>
#include<opencv2/opencv.hpp>

int main(int argc, char *argv[]) {
    cv::Mat src[10];
    for(int i=0; i < 10; ++i) {
        src[i] = cv::Mat::zeros(cv::Size(350, 350), CV_8UC3);
    }
    
	cv::circle(src[0], cv::Point(100,100), 50, cv::Scalar(255, 0, 0), -1);
	cv::circle(src[1], cv::Point(100,175), 50, cv::Scalar(0, 255, 0), -1);
	cv::circle(src[2], cv::Point(100,250), 50, cv::Scalar(0, 0, 255), -1);
    cv::imshow("src_0", src[0]);
    cv::imshow("src_1", src[1]);
    cv::imshow("src_2", src[2]);
    cv::imshow("src_02", src[0] + src[1] + src[2]);

    cv::circle(src[3], cv::Point(175,100), 50, cv::Scalar(0, 255, 0), -1);
    cv::circle(src[4], cv::Point(175,175), 50, cv::Scalar(0, 0, 255), -1);
    cv::circle(src[5], cv::Point(175,250), 50, cv::Scalar(255, 0, 0), -1);
    cv::imshow("src_3", src[3]);
    cv::imshow("src_4", src[4]);
    cv::imshow("src_5", src[5]);
    cv::imshow("src_35", src[3] + src[4] + src[5]);
	
    cv::circle(src[6], cv::Point(250,100), 50, cv::Scalar(0, 0, 255), -1);
    cv::circle(src[7], cv::Point(250,175), 50, cv::Scalar(255, 0, 0), -1);
    cv::circle(src[8], cv::Point(250,250), 50, cv::Scalar(0, 255, 0), -1);
    cv::imshow("src_6", src[6]);
    cv::imshow("src_7", src[7]);
    cv::imshow("src_8", src[8]);
    cv::imshow("src_68", src[6] + src[7] + src[8]);

    cv::add(src[6], src[7], src[9]);
    cv::imshow("src_67_9", src[9]);

//	cv::rectangle(src, cv::Point(100,100), cv::Point(250, 250), cv::Scalar(255, 255, 255), -1);

    cv::imshow("src_08", src[0] + src[1] + src[2] + src[3] + src[4] + src[5] + src[6] + src[7] + src[8] );

    cv::waitKey(0);
    cv::destroyAllWindows();
    return 0;
}


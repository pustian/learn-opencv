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

    cv::Mat channels[3];
    cv::split(src, channels);
    
    std::cout<<"width/cols="<< channels[0].cols
		<<" height/rows="<< channels[0].rows
		<<" channels="<< channels[0].channels()
		<<std::endl;
    cv::imshow("b", channels[0]);

    std::cout<<"width/cols="<< channels[1].cols
		<<" height/rows="<< channels[1].rows
		<<" channels="<< channels[1].channels()
		<<std::endl;
    cv::imshow("g", channels[1]);

    std::cout<<"width/cols="<< channels[2].cols
		<<" height/rows="<< channels[2].rows
		<<" channels="<< channels[2].channels()
		<<std::endl;
    cv::imshow("r", channels[2]);
    

    cv::waitKey(0);
    cv::destroyAllWindows();
    return 0;
}

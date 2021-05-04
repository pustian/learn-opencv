#include<opencv2/opencv.hpp>
#include<iostream>

void help(char** argv ) ;

int main(int argc, char* argv[]) { 
	cv::Mat src = cv::imread(argc>1?argv[1]:"./resources/panad.jpg");
    if(src.empty() ) {
        std::cout<<"Failed to open file"<<std::endl;
	    help(argv);
		return -1;
    }
    
    cv::imshow("origin", src);
    cv::waitKey(0);

    cv::destroyWindow("origin");

    return 0;
}

void help(char** argv ) {
	std::cerr<< "\n"
	<< "A simple OpenCV program that loads and displays an image from disk\n"
	<< argv[0] <<" <path/filename>\n"
	<< "For example:" << argv[0] << " ./resources/1.tif\n"
	<< std::endl;
}


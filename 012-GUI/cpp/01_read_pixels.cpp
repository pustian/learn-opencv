#include<opencv2/opencv.hpp>
#include<iostream>

void mat_info(cv::Mat& mat);
cv::Mat& access_pixles(cv::Mat& mat);

int main() { 
    cv::Mat src = cv::imread("./resources/3.tif");
    if(src.empty() ) {
        std::cout<<"Failed to open file"<<std::endl;
	return -1;
    }
    
    cv::imshow("origin", src);

    mat_info(src);

	access_pixles(src);

    cv::imshow("reserve", src);
    
    cv::waitKey(0);
    cv::destroyWindow("origin");

    return 0;
}

void mat_info(cv::Mat& mat) {
    std::cout<<"height/rows="<<mat.rows
	    <<"\twidth/cols="<<mat.cols
	    <<"\tchannels="<<mat.channels()
	    <<"\ttotal="<<mat.total()
	    <<std::endl;
}
cv::Mat& access_pixles(cv::Mat& mat) {
    // 直接读取图像像素
	int height = mat.rows;
	int width = mat.cols;
	int ch = mat.channels();
	int bgr[3];
	for (int row = 0; row < height; row++) {
		// 像素取反
		for (int col = 0; col < width; col++) {
			if (ch == 3) {
				cv::Vec3b bgr = mat.at<cv::Vec3b>(row, col);
				bgr[0] = 255 - bgr[0];
				bgr[1] = 255 - bgr[1];
				bgr[2] = 255 - bgr[2];
				mat.at<cv::Vec3b>(row, col) = bgr;
				if((10<bgr[0] && bgr[0] <240) 
						|| (10<bgr[1] && bgr[1] <240 )
						|| (10<bgr[2] && bgr[2] <240 )
				  ){
					printf("%d %d %d %d %d:");
				}
			} else if (ch == 1) {
				int gray = mat.at<uchar>(row, col);
				mat.at<uchar>(row, col) = 255 - gray;
			}
		}
	}

    return mat;
}

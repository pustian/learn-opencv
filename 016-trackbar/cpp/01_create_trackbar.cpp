#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
void on_change(int x, void* ) {
    std::cout<<x<<std::endl;
}

int main(int argc, char *argv[]) {
    Mat mat = Mat::zeros(Size(600, 400), CV_8SC1);
  
    std::cout<<"width/cols="<<mat.cols
        <<" height/rows="<<mat.rows
		<<" channels="<<mat.channels()
		<<std::endl;
    
    std::string winname = "origin";
    cv::namedWindow(winname);
    for(int row=0; row<mat.rows; ++row) {
        for(int col=0; col<mat.cols; ++col) {
			mat.at<uchar>(row, col) = 255 - col*row % 255;
        }
    }
    imshow(winname, mat);

    std::string winname2 = "origin_color";
    std::string trackbarname = "color";
    int begin_color = 100;
    imshow(winname2 , mat);
    createTrackbar(trackbarname, winname2, &begin_color, 255, on_change);
     
    while(true) {
        int val = getTrackbarPos(trackbarname, winname2);
        for(int row=mat.rows/2; row<mat.rows; ++row) {
            for(int col=mat.cols/2; col<mat.cols; ++col) {
	    		int gray = mat.at<uchar>(row, col);
                if(gray > val) {
	    		    mat.at<uchar>(row, col) = gray;
                } else {
	    		    mat.at<uchar>(row, col) = 255-gray;
                }
            }
        }

        imshow(winname2 , mat);
        if (waitKey(1) == 'q') 
            break;
    }

    destroyAllWindows();

    return 0;
}

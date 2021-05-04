#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
using namespace std;

Mat *g_mat;
void show_pixel(int event, int x, int y, int flags, void* ) {
	if(event == EVENT_FLAG_MBUTTON ) {
		cv::Vec3b bgr = g_mat->at<cv::Vec3b>(y, x);
		bgr[0] = 255 - bgr[0];
		bgr[1] = 255 - bgr[1];
		bgr[2] = 255 - bgr[2];
		cout<<"x="<<x <<" y="<<y
			<<"[b="<<static_cast<int>(bgr[0])
			<<" g="<<static_cast<int>(bgr[1])
			<<" r="<<static_cast<int>(bgr[2])<<"]"<<endl;
	}
}

int main(int argc, char* argv[]) {
	Mat src = imread(argc>1?argv[1]:"./resources/tiger.jpeg");
    if(src.empty() ) {
		cerr<<"imread failed"<<endl;
		return -1;
	}

	g_mat = &src;

	imshow("origin", src);
	setMouseCallback("origin", show_pixel);

	waitKey(0);
	destroyAllWindows();
    return 0;
}


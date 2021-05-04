#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
void on_change(int x, void* ) {
    std::cout<<x<<std::endl;
}

int main(int argc, char *argv[]) {
    Mat mat = imread(argc>1?argv[1]:"./resources/panad.jpg", IMREAD_GRAYSCALE);
    if(mat.empty() ) {
        return -1;
    }
  
    std::cout<<"width/cols="<<mat.cols
        <<" height/rows="<<mat.rows
		<<" channels="<<mat.channels()
		<<std::endl;
    
    std::string winname_color = "origin_color";
    imshow(winname_color, mat);

    Mat dst;
    mat.copyTo(dst);
    std::string threshold_winname= "threshold_color";
    imshow(threshold_winname, dst);
    int color = 100;
    std::string trackbar_name = "color";
    createTrackbar(trackbar_name,  threshold_winname, &color, 255, on_change);


    while(true) {
        int color= getTrackbarPos(trackbar_name, threshold_winname);
        
        threshold(mat, dst, color, 255, THRESH_BINARY);
        imshow(threshold_winname, dst);

        if (waitKey(1) == 'q') 
            break;
    }

    waitKey(0);
    destroyAllWindows();

    return 0;
}

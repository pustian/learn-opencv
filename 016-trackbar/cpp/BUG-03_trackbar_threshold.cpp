#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
void on_change(int x, void* ) {
    std::cout<<x<<std::endl;
}

int main(int argc, char *argv[]) {
    Mat mat = imread(argc>1?argv[1]:"./resources/tiger.jpeg");
    if(mat.empty() ) {
        return -1;
    }
  
    std::cout<<"width/cols="<<mat.cols
        <<" height/rows="<<mat.rows
		<<" channels="<<mat.channels()
		<<std::endl;
    
    std::string winname_color = "origin_color";
    std::string trackbar_name_b = "b";
    std::string trackbar_name_g = "g";
    std::string trackbar_name_r = "r";
    int b_color = 100;
    int g_color = 100;
    int r_color = 100;
//    imshow(winname_color, mat);
//    createTrackbar(trackbar_name_b, winname_color, &b_color, 255, on_change);
//    createTrackbar(trackbar_name_g, winname_color, &g_color, 255, on_change);
//    createTrackbar(trackbar_name_r, winname_color, &r_color, 255, on_change);

    Mat b_mat = mat.clone();
    Mat g_mat = mat.clone();
    Mat r_mat = mat.clone();
    int bgr_0, bgr_1, bgr_2;
    cv::Vec3b b, g, r; 
    for (int row = 0; row < mat.rows; ++row) {
        for (int col = 0; col < mat.cols; ++col) {
            cv::Vec3b& bgr = mat.at<cv::Vec3b>(col, row);
            b[0] = bgr[0]; b[1]=0; b[2]=0;
            b_mat.at<cv::Vec3b>(col, row) = b;
            g[0] = 0; g[1]=bgr[1]; g[2]=0;
            g_mat.at<cv::Vec3b>(col, row) = g;
            r[0] = 0; r[1]=0; r[2]=bgr[2];
            r_mat.at<cv::Vec3b>(col, row) = r;
        }
    }
    imshow("b_", b_mat);
    imshow("g_", g_mat);
    imshow("r_", r_mat);

//    while(true) {
//        int b_color= getTrackbarPos(trackbar_name_b, winname_color);
//        int g_color= getTrackbarPos(trackbar_name_g, winname_color);
//        int r_color= getTrackbarPos(trackbar_name_r, winname_color);
//        
//        threshold(b_color, b_mat, b_color, 255, THRESH_BINARY);
//        threshold(g_color, g_mat, g_color, 255, THRESH_BINARY);
//        threshold(r_color, r_mat, r_color, 255, THRESH_BINARY);
//    imshow("b_", b_mat);
//    imshow("g_", g_mat);
//    imshow("r_", r_mat);
//
//
//        if (waitKey(1) == 'q') 
//            break;
//    }

    waitKey(0);
    destroyAllWindows();

    return 0;
}

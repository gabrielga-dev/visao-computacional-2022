import cv2

img = cv2.imread('carro.jpg')

img = img[130:300, 100:600] # Crop from x, y, w, h -> 100, 200, 300, 400

#            y:h, x,w
cv2.imshow('img',img)
cv2.waitKey(0)
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
#cv2.imshow('bin', bin)

desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
#cv2.imshow('des', desfoque)

contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

"""
//Em java
//pega imagem colunas e linhas
Mat src = imread("your image"); int row = src.rows; int col = src.cols;
//Create contour
vector<vector<Point> > contours; 
vector<Vec4i> hierarchy;
Mat src_copy = src.clone();
findContours( src_copy, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE);

// Create Mask
Mat_<uchar> mask(row,col);    
for (int j=0; j<row; j++)
    for (int i=0; i<col; i++)
        {
            if ( pointPolygonTest( contours[0], Point2f(i,j),false) =0)
            {mask(j,i)=255;}
            else
            {mask(j,i)=0;}
        };
"""


#cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
#cv2.imshow('cont', img)

for c in contornos:
    print (len(c))
    perimetro = cv2.arcLength(c, True)
    if perimetro > 120:
        aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)
        if len(aprox) == 4:
            (x, y, alt, lar) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+alt, y+lar), (0, 255, 0), 2)
            roi = img[y:y + lar, x:x + alt]
            cv2.imwrite('res/roi.jpg', roi)


cv2.imshow('draw', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
        Mat cannyOutput = new Mat();
        Imgproc.Canny(srcGray, cannyOutput, threshold, threshold * 2);
        List<MatOfPoint> contours = new ArrayList<>();
        Mat hierarchy = new Mat();
        Imgproc.findContours(cannyOutput, contours, hierarchy, Imgproc.RETR_TREE, Imgproc.CHAIN_APPROX_SIMPLE);
        Mat drawing = Mat.zeros(cannyOutput.size(), CvType.CV_8UC3);
        for (int i = 0; i < contours.size(); i++) {
            Scalar color = new Scalar(rng.nextInt(256), rng.nextInt(256), rng.nextInt(256));
            Imgproc.drawContours(drawing, contours, i, color, 2, Core.LINE_8, hierarchy, 0, new Point());
        }
        imgContoursLabel.setIcon(new ImageIcon(HighGui.toBufferedImage(drawing)));
        frame.repaint();
"""

"""
Mat image;
// read the input image
image = imread("D:\\omr.jpg");

Mat gray;
cvtColor(image, gray, CV_BGR2GRAY);

GaussianBlur(gray, gray, Size(5,5) , 0, 0);

Mat thres;
threshold(gray, thres, 130, 255, CV_THRESH_BINARY_INV);
imshow("thres", thres);
waitKey();


//  apply a connected component analysis with statistics
//  (from opencv 3.0 onwards)
// cca
Mat labels, stats, centroids;
int numObjects = connectedComponentsWithStats(thres, labels, stats, centroids);

// Draw bounding boxes for objects in the original image
// exclude background = 0
int i;
for(i=1; i<numObjects; i++)
{
    int left = stats.at<int>(i, CC_STAT_LEFT);
    int top = stats.at<int>(i, CC_STAT_TOP);
    double width = stats.at<int>(i, CC_STAT_WIDTH);
    double height = stats.at<int>(i, CC_STAT_HEIGHT);
    int area = stats.at<int>(i, CC_STAT_AREA);

    double k = width/height;

    if(area > 500 && area < 2000 && k > 0.9 && k < 1.1)
    {
        // draw rectangle
        rectangle(image, Rect(left, top, width, height), Scalar(0,255,0), 2);
    }
}

imshow("BoundingBoxes", image);
"""

"""
@Override
public Mat onCameraFrame(CameraBridgeViewBase.CvCameraViewFrame inputFrame) {
    mRgba = inputFrame.rgba();
    contours = new ArrayList<MatOfPoint>();
    hierarchy = new Mat();
    Imgproc.GaussianBlur(mRgba,mIntermediateMat,new Size(9,9),2,2);
    Imgproc.Canny(mRgba, mIntermediateMat, 80, 100);
    Imgproc.findContours(mIntermediateMat, contours, hierarchy, Imgproc.RETR_TREE, Imgproc.CHAIN_APPROX_SIMPLE, new Point(0, 0));
/* Mat drawing = Mat.zeros( mIntermediateMat.size(), CvType.CV_8UC3 );
 for( int i = 0; i< contours.size(); i++ )
 {
Scalar color =new Scalar(Math.random()*255, Math.random()*255, Math.random()*255);
 Imgproc.drawContours( drawing, contours, i, color, 2, 8, hierarchy, 0, new Point() );
 }*/
    hierarchy.release();
            // Imgproc.cvtColor(mIntermediateMat, mRgba, Imgproc.COLOR_GRAY2RGBA, 4)
/* Mat drawing = Mat.zeros( mIntermediateMat.size(), CvType.CV_8UC3 );
 for( int i = 0; i< contours.size(); i++ )
 {
Scalar color =new Scalar(Math.random()*255, Math.random()*255, Math.random()*255);
 Imgproc.drawContours( drawing, contours, i, color, 2, 8, hierarchy, 0, new Point() );
 }*/
    for ( int contourIdx=0; contourIdx < contours.size(); contourIdx++ )
    {
        // Minimum size allowed for consideration
        MatOfPoint2f approxCurve = new MatOfPoint2f();
        MatOfPoint2f contour2f = new MatOfPoint2f( contours.get(contourIdx).toArray() );
        //Processing on mMOP2f1 which is in type MatOfPoint2f
        double approxDistance = Imgproc.arcLength(contour2f, true)*0.02;
        Imgproc.approxPolyDP(contour2f, approxCurve, approxDistance, true);

        //Convert back to MatOfPoint
        MatOfPoint points = new MatOfPoint( approxCurve.toArray() );

        // Get bounding rect of contour
        Rect rect = Imgproc.boundingRect(points);

            Core.rectangle(mRgba, new Point(rect.x, rect.y), new Point(rect.x + rect.width, rect.y + rect.height), new Scalar(255, 0, 0, 255), 3);



    }
    return mRgba;
}
"""
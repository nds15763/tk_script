class DBMaskCreative:
    CreativeID :int
    VideoID:int
    PicID:int
    ContentID  :int
    ProductID :int

    def toModel(self,re):
        try:
            reDB = list[DBMaskCreative]
            for item in re:
                tmp = DBMaskCreative
                tmp.CreativeID = item[0]
                tmp.VideoID = item[1]
                tmp.PicID = item[2]
                tmp.ContentID = item[3]
                tmp.ProductID = item[4]
                reDB.append(tmp)
        except:
            print("DBMaskCreative toModel Error data:",re)
        
        return reDB

    def toModelFirstLine(self,re):
        try:
                tmp = DBMaskCreative
                tmp.CreativeID = re[0][0]
                tmp.VideoID = re[0][1]
                tmp.PicID = re[0][2]
                tmp.ContentID = re[0][3]
                tmp.ProductID = re[0][4]
        except:
            print("DBMaskCreative toModelFirstLine Error data:",re)
        
        return tmp
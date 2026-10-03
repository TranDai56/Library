from django.db import models

class Author(models.Model):
    #kiểu dữ liệu giống String trong python model.CharField(độ dài)
    #name dùng kiểu models.CharField(độ dài 100)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    #models.DateFiled(null,blank) 
    # null =True có nghĩa là để trống ngày tháng
    # blank nếu =True thì ko cần phk điền vào form còn False thì phk điền ko nó báo lỗi

    #ngày sinh của tác giá
    date_of_birth = models.DateField(null=True, blank=True)
    #ngày mất của tác giả

    date_of_death = models.DateField(null=True, blank=True)

    #hàm trả quy định cách đối tượng hiển thị dưới dạng gì
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#mối quan hệ
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)

    #textField(blank) đoạn văn bản dài đc phép để trống
    summary = models.TextField(blank=True)

    #mã số sách dưới dạng Sting
    #unique=true thì ko cho phép trùng lặp
    isbn = models.CharField(max_length=13, unique=True)

    #ForeignKey có tác dụng liên kết các bảng vs nhau thg là mối quan hệ 1-nhiều
    # mỗi liên hệ giữa tác giả và và quyển sách đó ( 1 tác giả thì 1 quyển sách)
    author = models.ForeignKey(
        Author,

        # on_delete=models.CASADE khi xóa tác giả thì xó luôn sách
        on_delete=models.CASCADE,

        # cho phép truy cập ngược lại từ sách lên tác giả
        related_name="books"
    )

    #ManytoManyFiled mối quan hệ nhiều nhiều
    # 1 sách có thể có nhiều loại sách khác nhau
    genres = models.ManyToManyField(
        Genre,
        related_name="books",
        #nếu ko có thể loại thì ko cần ghi
        blank=True
    )

    def __str__(self):
        return self.title


class BookCopy(models.Model):

    #các phương án chọn trạng thái sách
    STATUS_CHOICES = [
        ("Available", "Available"),
        ("On loan", "On loan"),
        ("Maintenance", "Maintenance"),
    ]
    #đây là Id của mỗi quyển sách
    id = models.UUIDField(primary_key=True)

    # đây là nhà xuất bản
    imprint = models.CharField(max_length=255)

    #trang thái sách
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,

        #nếu ko điền thì ở dạng available (có sẵn)
        default="Available"
    )
    #trả về ngày phk trả
    due_back = models.DateField(null=True, blank=True)

    #liên kết vs class Book ở trên
    book = models.ForeignKey(
        Book,
        #nếu xóa book thig book.copy cx phk xóa
        on_delete=models.CASCADE,
        #cho phép truy cập ngược lại book
        related_name="copies"
    )
    #trả về  tên sách và id của sách
    def __str__(self):
        return f"{self.book.title} - {self.id}"
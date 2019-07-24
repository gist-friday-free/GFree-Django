from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from api.models import Class, User, Notice, PlayStoreInfo, Review, Edit
from api.serializers import ClassSerializer, UserSerializer, NoticeSerializer, PlayStoreInfoSerializer, \
    ReviewSerializer, EditSerializer


class ServerRunning(APIView):

    def get(self, request: Request, *args, **kwargs):
        return Response(True)


@api_view(['GET'])
def play_store_info(request, format=None):
    current_info = PlayStoreInfo.objects.first()
    serializer = PlayStoreInfoSerializer(current_info)

    return Response(serializer.data)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'classes': reverse('class-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'notices': reverse('notice-list', request=request, format=format),
        'reviews': reverse('review-list', request=request, format=format),
        'edits': reverse('edit-list', request=request, format=format),
    })


class ClassList(generics.GenericAPIView,
                mixins.CreateModelMixin):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get(self, request: Request, *args, **kwargs):
        year = request.query_params.get('year')
        semester = request.query_params.get('semester')

        code = request.query_params.get('code')

        if not year or not semester:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        result = self.queryset.filter(year__exact=year).filter(semester__exact=semester)

        # 코드가 존재한다면 일치하는 코드 1개 혹은 없는 것을 반환
        if code is not None:
            classData = result.filter(code__exact=code)
            if classData.exists():
                serializer: ClassSerializer = self.serializer_class(instance=result.get(code__exact=code))
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer: ClassSerializer = self.serializer_class(instance=result, many=True)
            return Response(serializer.data)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDetailUsers(APIView):

    def get(self, request, pk, *args, **kwargs):
        classData: Class = Class.objects.get(pk=pk)
        users = UserSerializer(instance=classData.user_set.all(), many=True)
        return Response(users.data)


class ClassDetailReviews(APIView):

    def get(self, request, pk, *args, **kwargs):
        classData: Class = Class.objects.get(pk=pk)
        reviews = ReviewSerializer(instance=classData.review_set.all(), many=True)
        return Response(reviews.data)


class ClassDataEdits(APIView):

    def get(self, request, pk, *args, **kwargs):
        classData: Class = Class.objects.get(pk__exact=pk)
        edits = EditSerializer(instance=classData.edit_set.all(), many=True)
        return Response(edits.data)


class EditList(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = Edit.objects.all()
    serializer_class = EditSerializer

    def get(self, request, *args, **kwargs):
        year = request.query_params.get('year')
        semester = request.query_params.get('semester')

        code = request.query_params.get('code')

        if year is None or semester is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if code is not None:
            edits = self.queryset.filter(editClass__code__exact=code,year__exact=year,semester__exact=semester)
            serializer = EditSerializer(instance=edits.all(), many=True)
            return Response(serializer.data)
        else:
            edits = self.queryset.filter(year__exact=year, semester__exact=semester)
            serializer = EditSerializer(instance=edits.all(), many=True)
            return Response(serializer.data)


    def post(self, request: Request, *args, **kwargs):
        print(request.body)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class EditDetail(APIView):

    def put(self, request : Request, pk:int):
        add = request.query_params.get('add')
        uid = request.query_params.get('uid')

        edit = Edit.objects.get(pk__exact=pk)
        user = User.objects.get(pk__exact=uid)

        print(user)

        print(edit)

        if add == '1':
            edit.star.add(user)
        else:
            edit.star.remove(user)
        print(edit.star.all())


        return Response(EditSerializer(instance=edit).data)

class EditUserList(APIView):

    def get(self, request : Request, pk : int,*args, **kwargs):
        edit:Edit = Edit.objects.get(pk__exact=pk)
        users=edit.star.all()

        return Response(UserSerializer(instance = users, many=True).data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request: Request, pk, *args, **kwargs):
        classData = request.query_params.get('classData')
        remove = request.query_params.get('remove')

        originalUser: User = User.objects.get(uid__exact=pk)

        serializer: UserSerializer = UserSerializer(originalUser, data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        print(serializer.data)
        if (classData is not None) and (remove is not None):
            user: User = User.objects.get(pk=pk)
            try:
                classData: Class = Class.objects.get(pk=classData)
                if remove == 'true':
                    user.classes.remove(classData)
                    print('class삭제 :', classData)
                else:
                    user.classes.add(classData)
                    print('class추가 :', classData)
                user.save()
            except Exception as e:
                print(e)
                pass

        return Response(self.serializer_class(originalUser).data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserClassList(APIView):

    def get(self, request: Request, pk, *args, **kwargs):
        year = request.query_params.get('year')
        semester = request.query_params.get('semester')

        try:
            user = User.objects.get(uid__exact=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        classes = user.classes.all()
        print(classes.all())
        if year and semester:
            classes = classes.filter(year__exact=year).filter(semester__exact=semester)
            print(classes.all())
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class NoticeList(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class NoticeDetail(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

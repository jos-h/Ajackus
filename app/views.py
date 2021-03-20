from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from .serializers import UserSerializer


class UserRegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            user_instance = User.objects.filter(email=data.get("email")).first()
            if user_instance:
                return Response(data="User already exists!!!!", status=status.HTTP_200_OK)
            else:
                s = UserSerializer(data=request.data)
            if s.is_valid(raise_exception=True):
                s.save()
                return Response(data=s.data, status=status.HTTP_201_CREATED)
        except (KeyError, ValidationError, Exception) as ex:
            return Response(data=ex.args, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):

    def post(self, request):
        try:
            data = request.data
            user_instance = User.objects.filter(email=data.get("email"), password=data.get("password")).first()
            if not user_instance:
                raise APIException(detail="user does not exists!!!!", code=status.HTTP_400_BAD_REQUEST)
            if user_instance:
                token_serializer = TokenObtainPairSerializer.get_token(user_instance)
                data.update(token=str(token_serializer.access_token))
                return Response(data=data, status=status.HTTP_200_OK)
        except (KeyError, ValidationError) as ex:
            return Response(data=ex.args, status=status.HTTP_400_BAD_REQUEST)


# class CreateContentView(APIView):
#
#     def post(self, request):
#         try:
#             data = request.data
#             file_object = self.create_pdf(data)
#             data.update(user=request.user.id, document=file_object)
#             content_instance = Content.objects.filter(user=request.user,
#                                                       title=data['title'],
#                                                       body=data['body']
#                                                       ).first()
#             content = ContentSerializer(instance=content_instance, data=data)
#             if content.is_valid(raise_exception=True):
#                 content.save()
#                 return Response(data=content.data, status=status.HTTP_201_CREATED)
#         except (KeyError, ValidationError) as ex:
#             return Response(data=ex.args, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         try:
#             queryset = Content.objects.filter(user=request.user)
#             content_serializer = ContentSerializer(queryset, many=True)
#             return Response(data=content_serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         try:
#             content_object = self.get_object(pk)
#             request_data = request.data
#             file_object = self.create_pdf(request.data)
#             request_data.update(user=request.user.id, document=file_object)
#             content_serializer = ContentSerializer(content_object, data=request.data)
#             if content_serializer.is_valid(raise_exception=True):
#                 content_serializer.save()
#                 return Response(data=content_serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         content = self.get_object(pk)
#         content.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             content = Content.objects.get(id=pk)
#             return content
#         except Content.DoesNotExist:
#             raise Http404
#
#     def create_pdf(self, data):
#         canvas = Canvas(data['title'] + ".pdf", pagesize=LETTER)
#         canvas.setFont("Times-Roman", 25)
#         canvas.setFillColor(black)
#         x, y = 30, 750
#         for each in data.keys():
#             canvas.drawString(x, y, data[each])
#             x += 5
#             y -= 100
#         buffer = io.BytesIO(canvas.getpdfdata())
#         return File(buffer, canvas._filename.rsplit("/")[-1])
#
#
# class DisplayContentView(generics.ListAPIView):
#     search_fields = ['title', 'body', 'summary']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer

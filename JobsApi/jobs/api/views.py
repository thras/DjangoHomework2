from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from jobs.models import JobOffer
from jobs.api.serializers import JobsSerializer
from rest_framework.generics import get_object_or_404


class JobsCreateAPIView(APIView):

    def get(self, request):
        jobs = JobOffer.objects.filter(available=True)
        serializer = JobsSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobsDetailAPIView(APIView):

    def get_object(self, pk):
        job = get_object_or_404(JobOffer,pk=pk)
        return job
    
    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobsSerializer(job)
        return Response(serializer.data)
    
    def put(self, request, pk):
        job = self.get_object(pk)
        serializer = JobsSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
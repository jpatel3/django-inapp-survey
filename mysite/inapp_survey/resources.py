from rest_framework import generics, mixins, permissions, \
    views, parsers, response, status
from rest_framework.response import Response

from inapp_survey.models import Campaign
from inapp_survey.serializers import CampaignSerializer, CampaignListSerializer

# TODO: Return the active campaign based on the information is passed in querystring
# param - will need to return based on that the first one.
class ActiveCampaignList(generics.ListAPIView):

    model = Campaign
    queryset = Campaign.objects.all()
    serializer_class = CampaignListSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ActiveCampaignDetails(generics.RetrieveAPIView):
    """Get the campaign details"""

    model = Campaign
    serializer_class = CampaignSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'slug'
    queryset = Campaign.objects.all()


# resource to make user campaign
# resource to make user campaign answers

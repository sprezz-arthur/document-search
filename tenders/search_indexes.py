import PyPDF2
from haystack import indexes
from . import models


class TenderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    title = indexes.CharField(model_attr="title")
    description = indexes.CharField(model_attr="description")

    def get_model(self):
        return models.Tender

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def prepare_text(self, obj):
        contents = []
        for F in obj.files.all():
            if F.file:
                with F.file.open(mode="rb") as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    content = ""
                    for page in pdf_reader.pages:
                        contents += page.extract_text()
                    contents.append(content)
        return "".join(contents)


class FileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
    )

    def get_model(self):
        return models.File

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def prepare_text(self, obj):
        if obj.file:
            with obj.file.open(mode="rb") as f:
                pdf_reader = PyPDF2.PdfReader(f)
                contents = ""
                for page in pdf_reader.pages:
                    contents += page.extract_text()
                return contents


class OxeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
    )

    def get_model(self):
        return models.Oxe

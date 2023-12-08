import json

from google.cloud import language_v1


class GoogleCloudNL(object):
    def __init__(self):
        self.client = language_v1.LanguageServiceClient()

    def entity_sentiment_to_json(self, text_content: str) -> str:
        document_type_in_plain_text = language_v1.Document.Type.PLAIN_TEXT

        language = "en"
        document = {"content": text_content, "type_": document_type_in_plain_text, "language": language}
        encoding_type = language_v1.EncodingType.UTF8

        response = self.client.analyze_entity_sentiment(
            request={"document": document, "encoding_type": encoding_type}
        )

        response_data = {
            "entities": [],
            "language": response.language
        }

        for entity in response.entities:
            entity_info = {
                "name": entity.name,
                "type": language_v1.Entity.Type(entity.type_).name,
                "salience": entity.salience,
                "sentiment": {
                    "score": entity.sentiment.score,
                    "magnitude": entity.sentiment.magnitude
                },
                "metadata": dict(entity.metadata),
                "mentions": [
                    {
                        "text": mention.text.content,
                        "type": language_v1.EntityMention.Type(mention.type_).name
                    }
                    for mention in entity.mentions
                ]
            }
            response_data["entities"].append(entity_info)

        return json.dumps(response_data, indent=2)

    def entities_to_json(self, text_content: str) -> str:
        document_type_in_plain_text = language_v1.Document.Type.PLAIN_TEXT

        language = "en"
        document = {"content": text_content, "type_": document_type_in_plain_text, "language": language}
        encoding_type = language_v1.EncodingType.UTF8

        response = self.client.analyze_entities(
            request={"document": document, "encoding_type": encoding_type}
        )

        response_data = {
            "entities": [],
            "language": response.language
        }

        for entity in response.entities:
            entity_info = {
                "name": entity.name,
                "type": language_v1.Entity.Type(entity.type_).name,
                "metadata": dict(entity.metadata),
                "mentions": [
                    {
                        "text": mention.text.content,
                        "type": language_v1.EntityMention.Type(mention.type_).name
                    }
                    for mention in entity.mentions
                ]
            }
            response_data["entities"].append(entity_info)

        return json.dumps(response_data, indent=2)

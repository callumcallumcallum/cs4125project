from src.classifierStrategy import SVMStrategy, HistGBStrategy, SGDStrategy, AdaBoostingStrategy, MLPStrategy

class ClassifierFactory:
    def __init__(self):
        # Registry for reusing classifiers
        self.classifier_registry = {}

    def register_classifier(self, category_name, classifier_instance):
        """Registers a classifier instance for reuse."""
        self.classifier_registry[category_name] = classifier_instance

    def create_classifier(model_type):
        if model_type == "svm":
            return SVMStrategy()
        elif model_type == "histgb":
            return HistGBStrategy()
        elif model_type == "sgd":
            return SGDStrategy()
        elif model_type == "adaBoosting":
            return AdaBoostingStrategy()
        elif model_type == "mlp":
            return MLPStrategy()
        else:
            raise ValueError(f"Unknown model type: {model_type}")
        
    


def add_category(factory):
    new_category = input("Enter the name of the new category: ")
    sample_emails = []
    while True:
        email = input("Enter a sample email for this category (or type 'done' to finish): ")
        if email.lower() == 'done':
            break
        sample_emails.append(email)
    # Add category and classifier
    classifier = factory.create_classifier(new_category, sample_emails)
    print(f"New category '{new_category}' added successfully with {len(sample_emails)} sample emails.")

    

    @staticmethod
    def _initialize_strategy(model_type):
        """Helper to initialize a strategy based on model type."""
        strategies = {
            "svm": SVMStrategy,
            "histgb": HistGBStrategy,
            "sgd": SGDStrategy,
            "adaBoosting": AdaBoostingStrategy,
            "mlp": MLPStrategy,
        }
        if model_type not in strategies:
            raise ValueError(f"Unknown model type: {model_type}")
        return strategies[model_type]()
